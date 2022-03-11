#!/usr/bin/python3 



print('Content-type:text/html\n\n')
print('<html>') 
print('<head>') 
print('<title>Project SIBD</title>') 
print('</head>') 
print('<body>') 

print('<h3>Insert a new boat_sailor </h3>') 

print('<form action= "register_boat_sailor.cgi" method="post">') 

print('<p> id: <input type="text" name="id"/></p>') 
print('<p> iso_code: <input type="text" name="iso_code"/></p>') 

print('<p><input type="submit" value="Submit"/></p>') 
print('</form>') 
print('</body>') 
print('</html>') 