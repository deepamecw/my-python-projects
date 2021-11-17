
import sqlite3
con = sqlite3.connect('mynewsql.db')
c = con.cursor()
c.execute('''CREATE TABLE newtable (start,end,score)''')
def create():
  try:
     c.execute('''CREATE TABLE newtable (start,end,score)''')  
  except:
      pass
  def insert():
    c.execute("""INSERT INTO newtable (start,end,score) values (1 , 99 , 123)""")
  def select(verbose = True):
    sql = "SELECT * FROM mytable"
    recs = c.execute(sql)
    if verbose:
      for row in recs:
        print (row)
  db_path = r'C:\\Users\\User\\Desktop\\sql\\mynewsql.db'
  con = sqlite3.connect(db_path)
  c = con.cursor()
  create()
  insert()
  con.commit()
  select()
  c.close()


