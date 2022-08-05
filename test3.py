#this is code to connect pycharm to MySql server

import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="abhi@29894")
cursor = mydb.cursor()
cursor.execute("select employee_id,emp_mailid from sudhanshu.ineuron")
l=[]  #creating empty list
for i in cursor.fetchall():
    l.append(i)   #appending required column into list l

print(l)
print(type(l[0]))