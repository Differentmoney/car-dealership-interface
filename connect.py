import mysql.connector
import db_config as config

# Function to establish connection to cs6400_fall21_team005 MySQL Database
def getConnection():
  try:
    conn = mysql.connector.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, database=config.DB_DB)
    return True, conn
  except mysql.connector.Error as exc:
    _, message = exc.args
    return False, message 

#Checks if the user is in the database and returns user role
def validation(usr, pwd):
  conn = getConnection()
  print(conn[0])
  if conn[0]:
    cur = conn[1].cursor()
    cur.execute("SELECT role FROM User WHERE username = %s AND password = %s", (usr, pwd))
    result = cur.fetchall()
    if cur.rowcount == 1:
      return result[0][0]
    else:
      return False





