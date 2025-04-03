# Declaraciones de variables
vacio = {}
frutas = {"NA":"naranja", "LI":"limón", "PO":"pomelo", "LI":"líma", "MA":"mandarina"}

# Mostramos información
print(f"Frutas: {frutas}")
print(f"Frutas PO: {frutas["PO"]}")      # pomelo

print(f"Frutas PO: {frutas.get("PO")}")
print(f"Frutas ML: {frutas.get("ML")}")

print(f"Núm. de elementos: {len(frutas)}")

print(f"Frutas Claves: {frutas.keys()}")
print(f"Frutas Claves: {list(frutas.keys())}")

# Insertar y Modificar elementos
frutas["NA"] = "Sandia"
frutas["CI"] = "Ciruela"            # cuando la clave no existe, añade un nuevo elemento
print(f"Frutas: {frutas}")

frutas.update({"NA":"Naranja"})
frutas.update({"PL":"Platano"})     # cuando la clave no existe, añade un nuevo elemento
print(f"Frutas: {frutas}")

# Eliminar elementos
frutas.pop("NA")
del frutas["PL"]
print(f"Frutas: {frutas}")

# Recorrer los elementos
for key in frutas:
    print(f"{key} -> {frutas[key]}")
print("")

# Copiar
vacio = frutas.copy()
print(f"Vacio: {vacio}")

# Limpiar el diccionario
frutas.clear()
print(f"Frutas: {frutas}")