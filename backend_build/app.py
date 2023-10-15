# app.py - Dan Davis
# Queries db container and formats
# output to forward to smsgateway

import mysql.connector

# Define ro connection properties
user_config = {
    'user': 'user',
    'password': 'pass',
    'host': 'db',
    'database': 'Potatofacts',
    'raise_on_warnings': True
}

# Define rw connection properties
root_config = {
    'user': 'root',
    'password': 'pass',
    'host': 'db',
    'database': 'Potatofacts',
    'raise_on_warnings': True
}

# Create a ro db connection
cnx = mysql.connector.connect(**user_config)

# Create a cursor
cursor = cnx.cursor()

# Query for subsciber information
query = ("SELECT firstname,smsnumb,lastfact from subscriber")

# Exec query and populate sublist => list of lists holding name,number,lastfact
cursor.execute(query)
sublist = []
for name,smsnumb,lastfact in cursor:
  sublist.append([name,smsnumb,lastfact]) 

# Close db connection
cnx.close();cursor.close()
print(sublist)

# Create lastfact list
factlist = []
for sub in sublist:
  factlist.append(sub[2])
print(factlist)







