class Migrate:

    def extract_enum_statement(self, s):
        if "enum" in s:
            ret = [i for i in s.split(" ") if "enum" in i][0]
            return ret
        else:
            return ""

    def compose_enum_type(self, enum_statement, n):
        enteries = enum_statement.replace("enum", "")
        enum_type = f"CREATE TYPE enum_{n} as ENUM {enteries};\n"
        return enum_type

    def add_escape_char(self, s):
        words = s.split("'")
        for i, word in enumerate(words):
            if "\\" in word:
                if words[i - 1][-1] != "\\":
                    words[i - 1] += "E"
        s = "'".join(words)
        return s

    def migrate_mysql_postgresql(self, filename="test.sql", outputpostgresql="output/migratedpostgresql.sql"):

        f = open(filename, "r", encoding="utf-8")
        Lines = f.readlines()
        f.close()

        schemacount = 0
        querycount = 0  # number of query rows
        table_statement = ""
        enum_types_statements = ""
        num_enum_types = 0
        tablefound = False

        for line in Lines:

            sql_line = line.replace("`", '"')
            # sql_line = sql_line.upper()
            if sql_line.startswith("CREATE TABLE") or tablefound:
                if not tablefound:
                    print("Table found")
                tablefound = True
                schemacount += 1

                if "ENGINE" in sql_line or "DEFAULT CHARSET" in sql_line in sql_line:
                    if sql_line.startswith(")") and ";" in sql_line:
                        sql_line = ");\n"
                        tablefound = False
                    elif sql_line.startswith(")"):
                        sql_line = ")\n"
                    elif ";" in sql_line:
                        sql_line = ";\n"
                        tablefound = False
                    else:
                        continue
                if ";" in sql_line:
                    tablefound = True
                    if ")" in sql_line:
                        sql_line = ");\n"
                    else:
                        sql_line = ";\n"
                    tablefound = False
                    table_statement += sql_line
                    table_statement = enum_types_statements + table_statement
                    print("Table_statement done")
                    continue
                if sql_line.startswith(")"):
                    sql_line = ")"

                if "enum" in sql_line:
                    enum_line = self.extract_enum_statement(sql_line)
                    enum_types_statements += self.compose_enum_type(
                        enum_line, num_enum_types
                    )
                    sql_line = sql_line.replace(enum_line, f"enum_{num_enum_types}")
                    num_enum_types += 1

                if "int" in sql_line:
                    int_subline = [i for i in sql_line.split(" ") if "int" in i][0]
                    sql_line = sql_line.replace(int_subline, "int")

                if "AUTO_INCREMENT," in sql_line:
                    sql_line = (
                            "  "
                            + [i for i in sql_line.split(" ") if len(i) > 0][0]
                            + " SERIAL,\n"
                    )

                if "COMMENT" in sql_line:
                    sql_line = sql_line.split(" COMMENT")[0] + ",\n"

                if "unsigned" in sql_line:
                    column_name = [i for i in sql_line.split(" ") if len(i) > 0][0]
                    sql_line = sql_line.replace(
                        "unsigned", f"check ({column_name} > 0)"
                    )

                if "COLLATE" in sql_line:
                    words = sql_line.split(" ")
                    for i, word in enumerate(words):
                        if word == "COLLATE":
                            del words[i + 1]
                            del words[i]
                            sql_line = " ".join(words)
                            break

                sql_line = sql_line.replace("datetime", "timestamp(0)")
                # constraints
                if "PRIMARY KEY" in sql_line:
                    column = sql_line.split("(")[1].split(")")[0]
                    for i in table_statement.split("\n"):
                        if column in i:
                            column_statement = i.replace(",", " PRIMARY KEY,")
                            table_statement = table_statement.replace(
                                i, column_statement
                            )
                            break
                    continue

                if "UNIQUE KEY" in sql_line:
                    column = sql_line.split("(")[1].split(")")[0]
                    for i in table_statement.split("\n"):
                        if column in i:
                            column_statement = i.replace(",", " UNIQUE,")
                            table_statement = table_statement.replace(
                                i, column_statement
                            )
                            break
                    continue

                if "FOREIGN KEY" in sql_line:
                    new_line = "  FOREIGN KEY" + sql_line.split("FOREIGN KEY")[1]
                    last_o_bracket = new_line.rfind("(")
                    last_c_bracket = new_line.rfind(")")
                    substring = new_line[last_o_bracket: last_c_bracket + 1]
                    new_line = new_line.replace(substring, "")
                    new_line = new_line.replace(' "', ' ("').replace('" ', '") ')
                    new_line = new_line.replace("REFERENCES", "REFERENCES parent_table")
                    sql_line = new_line
                elif "KEY" in sql_line:
                    continue

                if "KEY" in sql_line:
                    continue
            elif sql_line.startswith("CREATE DATABASE "):
                # CREATE DATABASE IF NOT EXISTS core DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
                # CREATE DATABASE "demoapp" WITH OWNER "root" ENCODING 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';
                l = 0
                if sql_line.startswith("CREATE DATABASE IF NOT EXISTS "):
                    l = 30
                else:
                    l = 16
                sql_line = sql_line[l:len(sql_line)]
                tokens = sql_line.split(" ")
                for dbname in tokens:
                    if not dbname == '':
                        break
                sql_line = 'CREATE DATABASE ' + dbname + ' WITH OWNER "root" ENCODING \'UTF8\' LC_COLLATE = \'en_US.utf8\' LC_CTYPE = \'en_US.utf8\';'

            else:
                sql_line = line.replace("`", "")
                if "\\" in sql_line:
                    sql_line = self.add_escape_char(sql_line)
                querycount += 1

            table_statement += sql_line

        print(f"{schemacount} create table lines converted. Finished table create.")
        print(f"{querycount} query lines converted.")

        # Write result to disk
        # print('\n', table_statement)
        table_statement = table_statement + "\n"
        textfile = open(outputpostgresql, "w")
        a = textfile.write(table_statement)
        textfile.close()
        print("Written sql to " + outputpostgresql)