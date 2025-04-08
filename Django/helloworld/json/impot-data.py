import json
import sqlite3

def create_table(conn):
    """Crea la tabla Customers si no existe."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers_customer (
            CustomerID VARCHAR(5) NOT NULL PRIMARY KEY,
            CompanyName VARCHAR(40) NOT NULL,
            ContactName VARCHAR(30) NOT NULL,
            ContactTitle VARCHAR(30) NOT NULL,
            Address VARCHAR(60) NOT NULL,
            City VARCHAR(15) NOT NULL,
            Region VARCHAR(15),
            PostalCode VARCHAR(10) NOT NULL,
            Country VARCHAR(15) NOT NULL,
            Phone VARCHAR(24) NOT NULL,
            Fax VARCHAR(24)
        )
    ''')
    conn.commit()

def clear_table(conn):
    """Vacía la tabla Customers antes de insertar nuevos datos."""
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Customers')
    conn.commit()

def insert_data(conn, data):
    """Inserta los datos en la tabla Customers."""
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO Customers (
            CustomerID, CompanyName, ContactName, ContactTitle, 
            Address, City, Region, PostalCode, Country, Phone, Fax
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', [(
        item["CustomerID"], item["CompanyName"], item["ContactName"], item["ContactTitle"],
        item["Address"], item["City"], item["Region"], item["PostalCode"],
        item["Country"], item["Phone"], item["Fax"]
    ) for item in data])
    conn.commit()

def main(json_file, db_file):
    """Función principal para leer el JSON y guardar los datos en SQLite."""
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    conn = sqlite3.connect(db_file)
    #create_table(conn)
    clear_table(conn)
    insert_data(conn, data)
    conn.close()
    print("Datos insertados correctamente en la base de datos.")

if __name__ == "__main__":
    json_filename = "customer_utf8.json"  # Cambia esto si el archivo tiene otro nombre
    database_filename = "../db.sqlite3"
    main(json_filename, database_filename)