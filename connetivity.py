import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="your password",
  database="database_name",
auth_plugin="mysql_native_password"
)

cursor = mydb.cursor(buffered=True)
