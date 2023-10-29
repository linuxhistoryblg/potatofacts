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
        try:
            fact_text_list.append(cursor.fetchall()[0][0])
        except IndexError:
            print("Encountered EOF")
            fact_text_list.append('EOF')
    cursor.close()
    user_cnx.close()
    
    
    # Populate subscriber list (sublist) with next fact
    for i in range(len(sublist)):
        sublist[i][2] = fact_text_list[i].rstrip()
    
    print("Sublist", sublist)
    return sublist


# Call query_db:
sublist, fact_list = query_db()

# Populate next_fact_id: next_fact_id = current 'nextfact' + 1
next_fact_id = [item[2] + 1 for item in sublist]

# Populate user list: user_list = sublist[0]
user_list = [user[0] for user in sublist]

# Call substitute_fact_for_factid:
sublist = substitute_fact_for_factid(fact_list, sublist)

# If subscriber has received all facts, remove them from subscriber table
## Create new rw db connection:
root_cnx = mysql.connector.connect(**root_config)
root_cursor = root_cnx.cursor()

## loop sublist and delete any where sublist[i][2] == 'EOF'
for subscriber in sublist:
    if subscriber[2] == 'EOF':
        query = f"DELETE from `subscriber` WHERE `smsnumb` = '{subscriber[1]}'"
        root_cursor.execute(query)
        root_cnx.commit()
root_cursor.close()
root_cnx.close()

# Update nextfact field in db:
## Zip next_fact_id anduser list
user_and_next_fact = list(zip(next_fact_id, user_list))

## Create a rw db connection and cursor
root_cnx = mysql.connector.connect(**root_config)
root_cursor = root_cnx.cursor()

## Query for subsciber information
for fact_id,user_name in user_and_next_fact:
    query = f"UPDATE `subscriber` SET `nextfact`='{fact_id}' WHERE `firstname` = '{user_name}'"
    root_cursor.execute(query)
    root_cnx.commit()

root_cursor.close()
root_cnx.close()



# Todo:
# 1. Update subscriber:nextfact ++1 DONE (10/29)
# 2. Remove subscriber when they have received all available potatofacts DONE(10/29)
# 3. Make app.py run in a non-terminating loop
# 4. Send sublist into smsgateway api



