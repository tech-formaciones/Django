import pymssql

# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="localhost",
    port="1433",
    user="dbuser",
    password="demo",
    database="Northwind"
)

# Creamos un cursor para ejecutar comando en la base de datos
# Creamos un cursor que retorna Tuplas
cursor = connection.cursor()

# Creamos un cursor que retorna Diccionarios
cursor = connection.cursor(as_dict=True)

######################################################
# SELECT, leer registros de la base de datos
######################################################

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")

# print(cursor.fetchall())

# Mostar el contenido del cursor utilizando un WHILE
row = cursor.fetchone()
while (row):
    print(f"      ID: {row['CustomerID']}")
    print(f" Empresa: {row['CompanyName']} - {row['City']} ({row['Country']})\n")
    row = cursor.fetchone()
