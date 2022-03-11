#!/usr/bin/python3 
import psycopg2, cgi
import login 




print('Content-type:text/html\n\n')
print('<html>') 
print('<head>') 
print('<title>Project SIBD</title>') 
print('</head>') 
print('<body>') 
connection = None 

# for delete 

try: 




# Creating connection \
	
	connection = psycopg2.connect(login.credentials) 
	connection.autocommit = false
	cursor = connection.cursor() 
	# Making query see psycopg2 
	form = cgi.FieldStorage() 

	#getvalue uses the names from the form in previous page 
	name =  form.getvalue("name")
	year =  form.getvalue("year")
	iso_code =  form.getvalue("iso_code")
	id_owner =  form.getvalue("id_owner")
	cni =  form.getvalue("cni")
	iso_code_owner =  form.getvalue("iso_code_owner")
	mmsi = form.getvalue("mmsi")

	
	try : 
		sql = "INSERT INTO boat VALUES (%s, %s,%s,%s,%s,%s);"
		data = (name, year,cni,iso_code,id_owner,iso_code_owner)
		# Only inserting into boat_vhf if the mmsi isn't empty
		if mmsi != '':
			sql = "INSERT INTO boat VALUES (%s, %s,%s);"
			data = (mmsi,cni,iso_code)
		# Feed the data to the SQL query as follows to avoid SQL injection \
		cursor.execute(sql, data) 
	Exception as e: 

	# Print errors on the webpage if they occur \
	print('<h1>An error occurred.</h1>') 
	print('<p>\{}</p>'.format(e)) 
	# Commit the update (without this step the database will not change) \
	connection.commit() 

	# Closing connection \
	cursor.close() 

Exception as e: 

	# Print errors on the webpage if they occur \
	print('<h1>An error occurred.</h1>') 
	print('<p>\{\}</p>'.format(e)) 

finally: 

	if connection is not None: 
		connection.close() 
print('</body>') 
print('</html>') 