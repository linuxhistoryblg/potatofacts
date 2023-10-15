import mysql.connector
# TODO: Iterate through factlist to return list of facts where factid = factlist[item]
# Define ro connection properties
user_config = {
    'user': 'user',
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
query = "SELECT facttext from facts WHERE factid = %(factids)d"
cursor.execute(query, { 'factids':2})
print(cursor.fetchall())

# Close db connection
cnx.close();cursor.close()