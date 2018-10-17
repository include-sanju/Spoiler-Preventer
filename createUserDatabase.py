# creates database (for input) to store email id and TVshows of each user
import mysql.connector
import env

def createUserDatabase():
  mydb = mysql.connector.connect(host='localhost',user='root',passwd=env.DB_PASSWORD)
  mycursor = mydb.cursor(buffered = True)
  mycursor.execute("CREATE DATABASE IF NOT EXISTS TVseries")
  mydb = mysql.connector.connect(host='localhost',user='root',passwd=env.DB_PASSWORD, database = env.MYSQL_DB)
  mycursor = mydb.cursor(buffered = True)
  mycursor.execute("create table if not exists User_data(email VARCHAR(200) ,TVshows VARCHAR(200))")
  return mycursor,mydb