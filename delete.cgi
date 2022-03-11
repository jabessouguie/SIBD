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
		id = form.getvalue('id')
		iso_code = form.getvalue('iso_code')
		id = id.replace(' ', '') 
		iso_code = iso_code.replace(' ', '') 
		cursor = connection.cursor()
		sql = 'DELETE FROM owner WHERE id = %(id)s AND iso_code = %(iso_code)s;'
		data = {'id': id,'iso_code': iso_code}

		try:
			cursor.execute(sql, data)
			connection.commit()
			
		except Exception as e:
			print('<p>', e, '</p>')

		cursor.close()


	elif table =='boat':
		cni = form.getvalue('cni')
		iso_code = form.getvalue('iso_code')
		cni = cni.replace(' ', '') 
		iso_code = iso_code.replace(' ', '')
		cursor = connection.cursor()
		mmsi = form.getvalue('mmsi')
		if mmmsi !='':
			sql = 'DELETE FROM boat_vhf WHERE cni = %(cni)s AND iso_code = %(iso_code)s;'
			data = {'cni': cni,'iso_code': iso_code}
			cursor.execute(sql, data)
			connection.commit()


		sql = 'DELETE FROM boat WHERE cni = %(cni)s AND iso_code = %(iso_code)s;'
		data = {'cni': cni,'iso_code': iso_code}
		cursor.execute(sql, data)
		connection.commit()

		try:
			connection.commit()
			cursor.close()
			
		except Exception as e:
			print('<p>', e, '</p>')
		

	elif table =='sailor':
		id = form.getvalue('id')
		iso_code = form.getvalue('iso_code')

		id = id.replace(' ', '') 
		iso_code = iso_code.replace(' ', '') 

		cursor = connection.cursor()

		sql = 'DELETE FROM sailor WHERE id = %(id)s AND iso_code = %(iso_code)s;'
		data = {'id': id,'iso_code': iso_code}
		cursor.execute(sql, data)
	
		try:
			connection.commit()
			cursor.close()
			
		except Exception as e:
			print('<p>', e, '</p>')
		
	elif table =='reservation':
		connection.autocommit = False 
		cni = form.getvalue('cni')
		date = form.getvalue('date')
		iso_code_boat = form.getvalue('iso_code_boat')
		id_sailor = form.getvalue('id_sailor')
		iso_code_sailor = form.getvalue('iso_code_sailor')
		start_date = form.getvalue('start_date')
		end_date = form.getvalue('end_date')
		cni = cni.replace(' ', '') 
		iso_code_boat = iso_code_boat.replace(' ', '') 
		iso_code_sailor = iso_code_sailor.replace(' ', '') 
		id_sailor = id_sailor.replace(' ', '') 
		start_date = start_date.replace(' ', '') 
		end_date = end_date.replace(' ', '') 

		cursor = connection.cursor()

		sql = 'DELETE FROM trip WHERE cni = %(cni)s AND  iso_code_boat = %(iso_code_boat)s AND id_sailor = %(id_sailor)s AND  iso_code_sailor = %(iso_code_sailor)s AND start_date = %(start_date)s AND  end_date = %(end_date)s;'
		data = {'date': date,'cni': cni,'iso_code_boat': iso_code_boat,'id_sailor': id_sailor,'iso_code_sailor': iso_code_sailor,'start_date': start_date,'end_date': end_date}
		cursor.execute(sql, data)
		

		sql = 'DELETE FROM reservation WHERE cni = %(cni)s AND  iso_code_boat = %(iso_code_boat)s AND id_sailor = %(id_sailor)s AND  iso_code_sailor = %(iso_code_sailor)s AND start_date = %(start_date)s AND  end_date = %(end_date)s;'
		data = {'cni': cni,'iso_code_boat': iso_code_boat,'id_sailor': id_sailor,'iso_code_sailor': iso_code_sailor,'start_date': start_date,'end_date': end_date}
		cursor.execute(sql, data)
	
		connection.commit()
		cursor.close()
			
		
		
	
            
except Exception as e: 
	print('<h1>An error occurred.</h1>') 
	print('<p>', e, '</p>') 

finally: 

	if connection is not None: 
		connection.close() 

print('</body>') 
print('</html>') 