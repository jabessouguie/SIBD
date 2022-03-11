#!/usr/bin/python3 


print('Content-type:text/html\n\n')
print('<html>') 
print('<head>') 
print('<title>Project SIBD</title>') 
print('</head>') 
print('<body>') 

print('<h3>Insert a new reservation </h3>') 

print('<form action="register_reservation.cgi" method="post">') 
print('<p> cni: <input type="text" name= "cni"></p>') 
print('<p> iso_code_boat: <input type="text" name="iso_code_boat/></p>') 
print('<p> id_sailor: <input type="text" name="id_sailor"/></p>') 
print('<p> iso_code_sailor : <input type="text" name="iso_code_sailor"/></p>') 
print('<p> start_date: <input type="date" name="start_date"/></p>') 
print('<p> end_date: <input type="date" name="end_date"/></p>') 
print('<p><input type="submit" value="Submit"/></p>') 
print('</form>') 
print('</body>') 
print('</html>') 