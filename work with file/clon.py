with open('snow.jpg', 'rb') as a:
    clon = a.read()

with open('snow_clon.jpg', 'wb') as b:
    b.write(clon)