import sqlite3
""" CREATE TABLE EMPLOYEES_DATA (
    FIRST text,
    LAST text,
    pay integer
    ) 
    
INSERT INTO EMPLOYEES_DATA VALUES(
    'atul', 'krish', 202)
    
    """

from sqlite3.dbapi2 import connect
con = sqlite3.connect('atul.db')
print(con,"connection success")
c = con.cursor()
result = c.execute("""INSERT INTO EMPLOYEES_DATA VALUES(
    'safsa', 'a', 2022)""")
""" for a in result:
    print(a) """
con.commit()
con.close()
