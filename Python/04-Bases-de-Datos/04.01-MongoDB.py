from pymongo import MongoClient, collection
from bson.objectid import ObjectId
from pprint import pprint
import json

class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None

#########################################################
# Conectar con el servidor MongoDB
#########################################################
cliente = MongoClient("mongodb://localhost:27017/")

# adminDB = cliente.admin
# resultado = adminDB.command("serverStatus")
# print(resultado)

print(cliente.admin.command("serverStatus"))
print(cliente["admin"].command("serverStatus"))


#########################################################
# Listado de bases de datos y colecciones
#########################################################

print(cliente.list_database_names())

for db in cliente.list_database_names():
    print(f"DB: {db}")
    for collection in cliente[db].list_collection_names():
        print(f" -> {collection}")


#########################################################
# Posicionamiento en una colección
#########################################################

db = cliente.northwind
db = cliente["northwind"]
collection = db.customers
collection = db["customers"]

collection = cliente.northwind.customers
collection = cliente["northwind"]["customers"]

resultado = collection.find()
resultado = cliente.northwind.customers.find()
resultado = cliente["northwind"]["customers"].find()


#########################################################
# Consultas
#########################################################

# Todos los documentos coincidentes con el filtro
resultado = collection.find()
pprint(resultado)

# El primer documentos coincidente con el filtro
resultado = collection.find_one()
pprint(resultado)

resultado = collection.find()                                                               # Todos los documentos
resultado = collection.find({"Country": "USA"})                                             # Clientes, valor Country igual a USA
resultado = collection.find({"Country": {"$eq": "USA"}})                                    # Clientes, valor Country igual a USA
resultado = collection.find({"Country": {"$ne": "USA"}})                                    # Clientes, valor Country NO Igual a USA
resultado = collection.find({"Country": {"$in": ["USA", "Mexico"]}})                        # Clientes, valor Country igual a USA y Mexico
resultado = collection.find({"CustomerID": {"$regex": "DE"}})                               # Clientes, el ID del cliente finaliza por DE
resultado = collection.find({"Country": "USA", "City": "San Francisco"})                    # Clientes, valor Country igual a USA y City San Francisco
resultado = collection.find({"$and": [{"Country": "USA"}, {"City": "San Francisco"}]})      # Clientes, valor Country igual a USA y City San Francisco
resultado = collection.find({"$or": [{"Country": "USA"}, {"City": "Berlin"}]})              
resultado = collection.find({"$or": [{"Country": "USA"}, {"Country": "Germany"}]})              

resultado = collection.find({"Country": "USA"}) 
resultado = collection.find({"Country": "USA"}).limit(3)
resultado = collection.find({"Country": "USA"}).skip(5)
resultado = collection.find({"Country": "USA"}).skip(5).limit(5)

resultado = collection.find({"Country": "USA"}).sort("City")
resultado = collection.find({"Country": "USA"}).sort({"City": 1})
resultado = collection.find({"Country": "USA"}).sort({"City": -1})
resultado = collection.find().sort([("Country", 1), ("City", 1)])

while (resultado.alive == True):
    documento = resultado.next()
    # pprint(documento)             # Mostramos el documento completo
    # print("")
    print(f"{documento["CustomerID"]}# {documento["CompanyName"]} - {documento["City"]} ({documento["Country"]})")
    
print("")

# Insertar

cliente = Customer()
cliente.CustomerID = "DEMO1"
cliente.CompanyName = "Empresa Uno SL"
cliente.ContactName = "Borja Cabeza"
cliente.ContactTitle = "Gerente"
cliente.Address = "Calle Uno, SN"
cliente.PostalCode = "28000"
cliente.Region = "Madrid"
cliente.City = "Madrid"
cliente.Country = "España"
cliente.Phone = "900100900"
cliente.Fax = "900100901"

#pprint(cliente.__dict__)
id = collection.insert_one(cliente.__dict__).inserted_id
print(f"ID del documento: {id}")

cliente2 = {'Address': 'Calle Dos, SN',
            'City': 'Madrid',
            'CompanyName': 'Empresa Dos SL',
            'ContactName': 'Borja Cabeza',
            'ContactTitle': 'Gerente',
            'Country': 'España',
            'CustomerID': 'DEMO2',
            'Fax': '900100901',
            'Phone': '900100900',
            'PostalCode': '28000',
            'Region': 'Madrid'}

id = collection.insert_one(cliente2).inserted_id
print(f"ID del documento: {id}")

# Update

query = {"CustomerID": {"$eq": "ANATR"}}
documento = collection.find_one(query)
pprint(documento)

newValues = {"$set": {
    "ContactName": "Ana Sánchez",
    "PostalCode": "28023"
}}

resultado = collection.update_one(query, newValues);
print(f"{resultado.matched_count} encontrados")
print(f"{resultado.modified_count} modificados")
print(resultado)

# Eliminar

resultado = collection.delete_many({"Country": {"$in": ["USA", "Mexico"]}})
print(f"{resultado.deleted_count}" borrados)
print(resultado)