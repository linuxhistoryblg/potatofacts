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

def query_db():
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
    
    
    # Create nextfact list
    fact_list = []
    for item in sublist:
        fact_list.append(item[2])
    return sublist, fact_list

def substitute_fact_for_factid(fact_list, sublist):

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

    
    print("Subscriber facts: ", fact_text_list)
    print("Subscribers: ", sublist)
    
    # Populate subscriber list (sublist) with next fact
    for i in sublist:
        i[2] = fact_text_list[i[2] - 1].rstrip()
    
    return sublist


# Call query_db:
sublist, fact_list = query_db()
#print("Subscriber List: ", sublist)
#print("Nextfact_list: ", fact_list)

# Call substitute_fact_for_factid:
sublist = substitute_fact_for_factid(fact_list, sublist)
print(sublist)


## Todo:
## 1. Update subscriber:nextfact ++1
## 2. Send sublist into smsgateway api
#
## Create a ro db connection
#root_cnx = mysql.connector.connect(**root_config)
#
## Create a cursor
#root_cursor = root_cnx.cursor()
#
## Query for subsciber information
#for i in range(4,10):
#    query = f"UPDATE `subscriber` SET `nextfact`='{i}' WHERE `entid` = 1"
#    root_cursor.execute(query)
#    root_cnx.commit()
#
#root_cursor.close()
#root_cnx.close()
#







