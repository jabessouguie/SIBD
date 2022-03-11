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
	connection = psycopg2.connect(login.credentials) 
	cursor = connection.cursor() 
	
	form = cgi.FieldStorage() 
	id =  form.getvalue('id')
	iso_code =  form.getvalue('iso_code')
	birthdate =  form.getvalue('birthdate')


	sql = "INSERT INTO owner VALUES (%s, %s,%s)"
	data = (id,iso_code,birthdate)

	print('<p>\{}</p>'.format(sql % data)) 

	cursor.execute(sql, data) 

	connection.commit() 
	cursor.close() 

except Exception as e: 
	print('<h1>An error occurred.</h1>') 
	print('<p>\{}</p>'.format(e)) 

finally: 

	if connection is not None: 
		connection.close() 

print('</body>') 
print('</html>') 