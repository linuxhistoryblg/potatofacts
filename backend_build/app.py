'''
app.py - Dan Davis
Queries db container and formats
output to forward to smsgateway
'''

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
query_subscriber = "SELECT firstname,smsnumb,nextfact from subscriber"

# Exec query and populate sublist => list of lists holding name,number,nextfact
cursor.execute(query_subscriber)
sublist = []
for name, smsnumb, nextfact in cursor:
    sublist.append([name, smsnumb, nextfact])

# Close db connection
cnx.close()
cursor.close()
print("Subscriber List: ", sublist)

# Create nextfact list
fact_list = []
for item in sublist:
    fact_list.append(item[2])
print("Nextfact_list: ", fact_list)

# Open new db connection
user_cnx = mysql.connector.connect(**user_config)
cursor = user_cnx.cursor()

# Populate factextlist with next fact for subscriber
fact_text_list = []
for i in fact_list:
    cursor.execute(f'SELECT facttext FROM facts WHERE factid = {i}')
    fact_text_list.append(cursor.fetchall()[0][0])
cursor.close()
user_cnx.close()

# Populate subscriber list (sublist) with next fact
for subscriber in sublist:
    for facttext in fact_text_list:
        subscriber[2] = facttext

print(sublist)

# Todo:
# 1. Update subscriber:nextfact ++1
# 2. Send sublist into smsgateway api

# Create a ro db connection
root_cnx = mysql.connector.connect(**root_config)

# Create a cursor
root_cursor = root_cnx.cursor()

# Query for subsciber information
for i in range(4,10):
    query = f"UPDATE `subscriber` SET `lastfact`='{i}' WHERE `entid` = 1"
    root_cursor.execute(query)
    root_cnx.commit()

root_cursor.close()
root_cnx.close()








