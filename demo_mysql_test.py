import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sandeep",
  password="YES"
)

print(mydb) 