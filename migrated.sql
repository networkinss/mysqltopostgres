 CREATE TYPE enum_0 as ENUM ('type_1','type_2');
CREATE TABLE "test_table" (
  "id" SERIAL PRIMARY KEY,
  "id_2" int NOT NULL UNIQUE,
  "sting_line" varchar(255) NOT NULL,
  "type" enum_0 NOT NULL);
INSERT INTO orders VALUES (1,'2',E'McDonald\'s','type_1')

INSERT INTO orders VALUES (2,'1','KFC','type_2')