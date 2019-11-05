#Tuplas
#Se declaran con "(" y ")"
#Son inmutables y organizan datos igual que en las listas

datos_db=('132.248.1733.88','root','12345678')
print(datos_db[1])
datos_db=('132.248.1733.88','admin','12345678')
print(datos_db[1])
print(datos_db.index('admin'))
print(datos_db.count('12345678'))
