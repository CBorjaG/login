# myscript.py

import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\Claudia\Downloads\realclient\instantclient_19_8")
# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect("SYSTEM", "Cep66405502020$", "localhost:1521/xe")

cursor = connection.cursor()
cursor.execute("""
        SELECT id_commune, name
        FROM commune
        WHERE region_id = '6' """,
        )
for fname, lname in cursor:
    print("Values:", fname, lname)