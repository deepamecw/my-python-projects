
import sqlite3
from sqlite3.dbapi2 import Cursor
con = sqlite3.connect('atul.db')
cursor = con.cursor()
cmd1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY,location TEXT)"""

cursor.execute(cmd1)
cmd2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER  PRIMARY KEY, STORE_ID INTEGER,TOTAL_COST FLOAT,
FOREIGN KEY(store_id)REFERENCES stores(store_id)"""
cursor.execute(cmd2)
cursor.execute("INSERT INTO stores VALUES (21, 'Minneapolis, MN')")
cursor.execute("INSERT INTO stores VALUES (95, 'chicago, IL')")
cursor.execute("INSERT INTO stores VALUES (64, 'Iowa City, IA')")

cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")

cursor.execute("SELECT* FROM purchases")
results = cursor.fetchall()
print(results)

