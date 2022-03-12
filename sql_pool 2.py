import mysql.connector
import db_config as config
import os

# Function to establish connection to cs6400_fall21_team005 MySQL Database
def getConnection():
  try:
    conn = mysql.connector.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, database=config.DB_DB)
    return True, conn
  except mysql.connector.Error as exc:
    _, message = exc.args
    return False, message 

# Function to establish connection to MySQL Database
def getConnection2():
  try:
    conn = mysql.connector.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD)
    return True, conn
  except mysql.connector.Error as exc:
    _, message = exc.args
    return False, message 


# Creates and populates the cs6400_fall21_team005 database and tables
def createDB():
  conn = getConnection2()
  absolute_path = os.path.dirname(os.path.abspath(__file__))
  if conn[0]:
    cur = conn[1].cursor()
    filename = absolute_path + '/sql/create_db.sql'
    with open(filename) as f:
      cur.execute(f.read(), multi=True)


#Checks if the user is in the database and returns user role
def validation(usr, pwd):
  conn = getConnection()
  #print(conn[0])
  if conn[0]:
    cur = conn[1].cursor()
    cur.execute("SELECT role FROM User WHERE username = %s AND password = %s", (usr, pwd))
    result = cur.fetchall()
    if cur.rowcount == 1:
      return result[0][0]
    else:
      return False

# generate report for sales by color
def sales_by_color():
  conn = getConnection()
  absolute_path = os.path.dirname(os.path.abspath(__file__))
  if conn[0]:
    cur = conn[1].cursor()
    filename = absolute_path + '/sql/create_db.sql'
    with open(filename) as f:
      cur.execute(f.read(), multi=True)
    result = cur.fetchall()
    return result

