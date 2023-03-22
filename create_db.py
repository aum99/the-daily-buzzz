import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="aum150402",
   auth_plugin='mysql_native_password')

my_cursor = mydb.cursor()

# my_cursor.execute('CREATE DATABASE blog')
