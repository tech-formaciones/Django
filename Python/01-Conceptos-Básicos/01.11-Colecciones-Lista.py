import json

# Declaraciones de variables
vacia = []
frutas = ["naranja", "limón", "pomelo", "líma", "mandarina"]

# Mostrar contenido
print(f"Frutas: {frutas}")
print(f"Frutas Posición 2: {frutas[2]}")      # pomelo
print(f"Núm. de elementos: {len(frutas)}")
print(f"Repiticiones de Naranja: {frutas.count("naranja")}")

# Modificar la posición 2
frutas[2] = "fresa"
print(f"Frutas Posición 2: {frutas[2]}")      # antes pomelo ahora fresa

# Añadir nuevo elementos
frutas.append("manzana")
frutas.append("melón")
print(f"Frutas: {frutas}")

frutas.insert(1, "sandia")
print(f"Frutas: {frutas}")

frutas.extend(["platano", "pera"])
print(f"Frutas: {frutas}")

# Comprobar valores
print(f"SI Exite Melocotón en frutas: {"melocotón" in frutas}")
print(f"NO Exite Melocotón en frutas: {"melocotón" not in frutas}")

# Eliminar elementos de la lista
frutas.pop(5)   # mandarina
frutas.remove("naranja")
print(f"Frutas: {frutas}")

# Ordenar los elementos de la listas
frutas.reverse()
print(f"Frutas: {frutas}")

frutas.sort(reverse=True)
print(f"Frutas: {frutas}")

frutas.sort()
print(f"Frutas: {frutas}")

# Recorrer la lista
for fruta in frutas:
    print(f"-> {fruta}")
print("")

for index in range(len(frutas)):
    print(f"{index} -> {frutas[index]}")
print("")

# Copiar la lista
vacia = frutas.copy()
print(f"Vacia: {vacia}")

# Limpiar la lista
frutas.clear()
print(f"Frutas: {frutas}")