# mysql-to-postgres

The script to load mysql files into postgres database.

The notebook demonstrates the code that loads the given MySQL file line-by-line and submits in into a posgres databse
while adjusting the syntax accordingly.
The aticle about it https://betterprogramming.pub/convert-mysql-files-to-postgres-format-on-the-fly-1a9bde5a186b

# Requirement

Python 3.5

# Fork

This has been forked from: 
https://github.com/Megachell/mysql-to-postgres  
to 
https://github.com/networkinss/mysql-to-postgres.git  
Reason is the need of a python script which can be easily integrated into other projects.   
Some adjustments and additions were needed as well.  
So now the integration is very simple. Just copy the file migrate.py into your own project
and import/use "Migrate" as a normal Python class.


