# Set up db connection
import mysql.connector
from mysql.connector import errorcode

user_config = {
    'user': 'user',
    'password': 'pass',
    'host': 'db',
    'database': 'db',
    'raise_on_warnings': True
}

root_config = {
    'user': 'root',
    'password': 'pass',
    'host': 'db',
    'database': 'db',
    'raise_on_warnings': True
}

try:
  user_cnx = mysql.connector.connect(**user_config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  user_cnx.close()

print('closing after successful user connect')
user_cnx.close()

try:
  root_cnx = mysql.connector.connect(**root_config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  root_cnx.close()

print('closing after successful root connect')
root_cnx.close()