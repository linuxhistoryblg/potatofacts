# app.py - Dan Davis
# Queries db container and formats
# output to forward to smsgateway

import mysql.connector
from mysql.connector import errorcode
import time

def make_user_cnx():
  # Define connection properties
  user_config = {
      'user': 'user',
      'password': 'pass',
      'host': 'db',
      'database': 'Potatofacts',
      'raise_on_warnings': True
  }
  # Make db connection for user
  try:
    user_cnx = mysql.connector.connect(**user_config)
    time.sleep(1)
    print('closing after successful user connect')
    user_cnx.close()
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    user_cnx.close()

def make_root_cnx():
  # Define connection properties
  root_config = {
      'user': 'root',
      'password': 'pass',
      'host': 'db',
      'database': 'Potatofacts',
      'raise_on_warnings': True
  }
  # Make db connection for root
  try:
    root_cnx = mysql.connector.connect(**root_config)
    time.sleep(1)
    print('closing after successful root connect')
    root_cnx.close()
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    root_cnx.close()


# Test connect functions:
make_user_cnx()
make_root_cnx()