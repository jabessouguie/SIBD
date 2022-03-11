#!/usr/bin/python3 

import login 
import psycopg2, cgi



print('Content-type:text/html\n\n') 
print('<html>') 
print('<head>') 
print('<title>Project SIBD</title>') 
print('</head>') 
print('<body>') 
connection = None 

try: 

# Creating connection 
	
	connection = psycopg2.connect(login.credentials) 
	cursor = connection.cursor() 
	form = cgi.FieldStorage() 

	id =  form.getvalue("id")
	iso_code =  form.getvalue("iso_code")
	# Making query \
	sql = "INSERT INTO sailor VALUES (%s, %s);"
	data = (id,iso_code)
	# Feed the data to the SQL query as follows to avoid SQL injection \
	cursor.execute(sql, data) 
	# Commit the update (without this step the database will not change) \
	connection.commit() 
	# Closing connection \
	cursor.close() 

except Exception as e: 

	# Print errors on the webpage if they occur \
	print('<h1>An error occurred.</h1>') 
	print('<p>\{}</p>'.format(e)) 

finally: 

	if connection is not None: 
		connection.close() 
print('</body>') 
print('</html>') 