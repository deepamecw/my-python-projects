import sqlite3
con = sqlite3.connect("project.db")

cursor = con.cursor()
table1 = """CREATE TABLE IF NOT EXISTS
student_record(name TEXT ,age INTEGER, place TEXT)"""
cursor.execute(table1)
print(table1,"table created")
def insertData(name,age,place):
    qry = "insert into student_record(name,age,place) values (?,?,?);"
    con.execute(qry,(name,age,place))
    con.commit()
    print("user details added")
def updateData(name,age,place):
    qry = "update student_record set name = ?,age = ?,place = ? where id = ?:"
    con.execute(qry,(name,age,place))
    con.commit()
def delete(id):
    qry = "delete from student_record where id =?;"
    con.execute(qry,(id))
    con.commit()

print("""
1.INSERT
2.UPDATE
3.DELETE
4.SELECT
""")
ch = 1
while ch == 1:
    c = int(input("select your choice: "))
    if(c == 1):
        print("add new record")
        name = input("enter ypur name: ")
        age = int(input("enter your age: "))
        place = input("enter your place: ")
        insertData(name,age,place)

    elif(c == 2):
        print("edit a record")
        name = input("enter ypur name: ")
        age = int(input("enter your age: "))
        place = input("enter your place: ")
        updateData(name,age,place)
    elif(c == 3):
        print("delete a record")
        id = int(input("enter the number: "))
        delete(id)
    elif(c == 4):
        print("print all record")
    else:
        print("invalid selection")

    ch = int(input("enter 1 to continue: "))
print("thank you")