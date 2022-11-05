import os

from migrate import Migrate

print("Start migration from Mysql to Postgresql")
rootdir = "mysql/"
output = "output"
m = Migrate()
if not os.path.exists(output):
    os.mkdir(output)
# s = m.migrate_mysql_postgresql('mysql/mysql_schema.sql', output + "/customer.sql")
# exit(0)

for dirpath, dirs, files in os.walk(rootdir):
    for filename in files:
        fname = os.path.join(dirpath, filename)
        if fname.endswith('.sql'):
            print("Start to migrate: " + fname)
            s = m.migrate_mysql_postgresql(fname, output + "/" + filename)
            print("End of file " + fname + ".")

        # print(os.path.join(rootdir, filename))
# for filename in glob.iglob(rootdir + '**/*.sql', recursive=True):
#      print(filename)


print("End migration from Mysql to Postgresql")
