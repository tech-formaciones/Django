# Declaración de variables
#        012345678901234567890      <--- Posiciones
texto = "    hola mundo !!!   "
print(texto)
print("")
print(f"Posición 5: {texto[5]}")
print(f"Desde posición 3 (incluida) : {texto[3:]}")
print(f"Hasta posición 6 (NO incluida) : {texto[:6]}")
print(f"Entre posición 3 y 6 (6 NO incluida) : {texto[3:6]}")
print(f"El 4 caracter empezando por el final: {texto[-4]}")
print("")

# Funciones para textos
print(f"Número de caractéres: {len(texto)}")
print(texto.lower())
print(texto.upper())
print(texto.strip().capitalize())
print(texto.title())
print(texto.capitalize())
print(texto.count("o"))
print(f"Es un digito: {texto.isdigit()}")
print(f"Es un digito: {"12".isdigit()}")
print("")


# Formatear Texto
mensaje = "Mundo"
print(f"Hola {mensaje} !!!")

# Formatear Números
numero = 10 / 3
print("Resultado:", numero)
print(f"Resultado: {numero:1.2f}")