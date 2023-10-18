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
query = ("SELECT firstname,smsnumb,nextfact from subscriber")

# Exec query and populate sublist => list of lists holding name,number,nextfact
cursor.execute(query)
sublist = []
for name,smsnumb,nextfact in cursor:
  sublist.append([name,smsnumb,nextfact]) 

# Close db connection
cnx.close();cursor.close()
print(sublist)

# Create nextfact list
factlist = []
for item in sublist:
  factlist.append(item[2])
print(factlist)

# Open new db connection
user_cnx = mysql.connector.connect(**user_config)
cursor = user_cnx.cursor()

# Populate factextlist with next fact for subscriber
facttextlist = []
for i in factlist:
    cursor.execute(f'SELECT facttext FROM facts WHERE factid = {i}')
    facttextlist.append(cursor.fetchall()[0][0])
cursor.close()
user_cnx.close()

# Populate subscriber list (sublist) with next fact
for subscriber in sublist:
    for facttext in facttextlist:
       subscriber[2] = facttext

print(sublist)

## Todo: 
# 1. Update subscriber:nextfact ++1
# 2. Send sublist into smsgateway api







