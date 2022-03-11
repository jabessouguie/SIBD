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
	form = cgi.FieldStorage() 
	table =  form.getvalue('table')

	if table =='owner':
		cursor = connection.cursor() 
		sql = 'SELECT * FROM owner;'
		cursor.execute(sql)
		result = cursor.fetchall()
		print('<table border="5">')
		print('<tr><th>id</th><th>iso_code</th><th>birthdate</th></tr>')
	
		for row in result:
			print('<tr>')
			print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2],  '</td><td> <a href="delete.cgi?table=owner&id=',row[0],'&iso_code=',row[1],'" >delete</a> </td>')
			print('</tr>')
		print('</table>')
		cursor.close()
	elif table =='boat':
		cursor = connection.cursor() 
		sql = 'SELECT * FROM boat;'
		cursor.execute(sql)
		result = cursor.fetchall()
		print('<table border="5">')
		print('<tr><th>name</th><th>year</th><th>cni</th><th>iso_code</th><th>id_owner</th><th>iso_code_owner</th></tr>')
	
		for row in result:
			print('<tr>')
			print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2],  '</td><td>', row[3], '</td><td>', row[4], '</td><td>', row[5],  '</td><td> <a href="delete.cgi?table=boat&cni=',row[2],'&iso_code=',row[3],'" >delete</a> </td>')
			print('</tr>')
		print('</table>')
		cursor.close()

	elif table =='sailor':
		cursor = connection.cursor() 
		sql = 'SELECT * FROM sailor;'
		cursor.execute(sql)
		result = cursor.fetchall()
		print('<table border="5">')
		print('<tr><th>id</th><th>iso_code</th></tr>')
	
		for row in result:
			print('<tr>')
			print('<td>', row[0], '</td><td>', row[1], '</td><td> <a href="delete.cgi?table=sailor&id=',row[0],'&iso_code=',row[1],'" >delete</a> </td>')
			print('</tr>')
		print('</table>')
		cursor.close()
	
	elif table =='reservation':
		cursor = connection.cursor() 
		sql = 'SELECT * FROM reservation;'
		cursor.execute(sql)
		result = cursor.fetchall()
		print('<table border="5">')
		print('<tr><th>cni</th><th>iso_code_boat</th><th>id_sailor</th><th>iso_code_sailor</th><th>start_date</th><th>end_date</th><th>delete</th></tr>')
	
		for row in result:
			print('<tr>')
			print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2],  '</td><td>', row[3], '</td><td>', row[4], '</td><td>', row[5],  '</td><td> <a href="delete.cgi?table=reservation&cni=',row[0],'&iso_code_boat=',row[1],'&id_sailor=',row[2],'&iso_code_sailor=',row[3],'&start_date=',row[4],'&end_date=',row[5],'" >delete</a> </td>')
			print('</tr>')
		print('</table>')
		cursor.close()
	
            
except Exception as e: 
	print('<h1>An error occurred.</h1>') 
	print('<p>\{}</p>'.format(e)) 

finally: 

	if connection is not None: 
		connection.close() 

print('</body>') 
print('</html>') 