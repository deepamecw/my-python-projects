import sqlite3
con = sqlite3.connect("atul.db")
""" CREATE TABLE USERDETAIL (
    NAME,
    AGE,
    CITY,
    GENDER
    ) 
    
    """

print(con,"connection success")
def insertData(NAME,AGE,CITY,GENDER):
    qry = "insert into  (name,age,place,gender) values (?,?,?,?);"
    con.execute(qry,(name,age,place,gender))
    con.commit()
    print("user details added")

print("""
1.insert
2.update
3.delete
4.select
""")
ch = 1
while ch == 1:
    c = int(input("enter your choice:" ))
    if(c == 1):
        print("new insertion")
        name = input("enter your name: ")
        age = input("enter your age: ")
        place = input("enter your place: ")
        gender = input("enter your gender: ")
        insertData(name,age,place,gender)
    elif(c == 2):
        print("new update")
    elif(c == 3):
        print("delete ")
    elif(c == 4):
        print("select ur ")
    else:
        print("invalid selection")
    ch =int(input("enter 1 to continue: "))
    print("thank you")
