#!/usr/bin/python3


print('Content-type:text/html\n\n')
print('<html>') 
print('<head>') 
print('<title>Project SIBD </title>') 
print('</head>') 
print('<body>') 

print('<h3>Insert a new boat </h3>') 

print('<form action= "register_boat.cgi" method="post">') 

print('<p> name: <input type="text" name="name"/></p>') 
print('<p> year: <input type="number" name="year"/></p>') 
print('<p> iso_code: <input type="text" name="iso_code"></p>') 

print('<p> id_owner: <input type="text" name="id_owner"></p>') 
print('<p> cni: <input type="text" name="cni"></p>') 
print('<p> iso_code_owner: <input type="text" name="iso_code_owner"></p>') 
print('<p> mmsi: <input type="text" name="mmsi"></p>') 

print('<p><input type="submit" value="Submit"/></p>') 
print('</form>') 
print('</body>') 
print('</html>') 