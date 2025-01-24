import mysql.connector

db_connection= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password123#",
    database="curd_op"
)

curddb=db_connection.cursor()
curddb.execute("Create database curd_op")
print("database created successfully")

curddb.execute("Create table details_tb (id int auto_increment primary key,name varchar(25),city varchar(20),age int(5))")
print("table created successfully")
db_connection.commit()


def insert(name,city,age):
    curddb=db_connection.cursor()
    sql="insert into details_tb (name,city,age) values(%s,%s,%s)"
    details_tb=(name,city,age)
    curddb.execute(sql,details_tb)
    print("Data insert success")

def update(name,city,age):
    curddb=db_connection.cursor()
    sql="update details_tb set name=%s,city=%s,age=%s where id =%s"
    details_tb=(name,city,age,id)
    curddb.execute(sql,details_tb)

def select():
    curddb=db_connection.cursor()
    sql="Select ID,NAME,AGE,CITY from details_tb"
    curddb.execute(sql)
    #result=curddb.fetchone()
    result=curddb.fetchall()
    print(result)

def delete():
    curddb=db_connection.cursor()
    sql="delete from details_tb where id=%s"
    details_tb=[id]
    curddb.execute(sql,details_tb)
    db_connection.commit()
    print("data deleted success")

def quite():
    curddb.close()
    db_connection.close()
    print("Exiting the program...")
    exit()

while True:
    print("1.Insert data into TB")
    print("2.Update from into TB")
    print("3.Select data into TB")
    print("4.Delete data from TB")
    print("5.Exit")

    choice=int(input("enter your choice:"))
    if choice==1:
        name =input("Enter Name: ")
        city=input("Enter City: ")
        age=input("Enter your age: ")
        insert(name,city,age)
    elif choice==2:
        name =input("Enter Name: ")
        city=input("Enter City: ")
        age=input("Enter your age: ")
        update(name,city,age)
    elif choice==3:
        select()
    elif choice==4:
        id =input(" Enter the ID to delete: ")
        delete()
    elif choice==5:
        quite()
    else:
        print("Invaild operation pls try again")
