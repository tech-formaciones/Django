# Declaración de variables
citricos = ["narajan", "limón", "pomelo", "líma", "mandarina"]

index = 0
while (index < len(citricos)):
    print(f"{index} -> {citricos[index]}")
    index += 1
print("")

numero = 0
while (numero < 8):
    numero += 1
    if (numero == 3):
        continue
    print(f"Numero: {numero}")
else:
    print(f"Sentencias WHILE finalizado o no iniciado")

# No existe DO/WHILE
# Lo simulamos incluyendo la condición al final del bloque de While, cuando no se cumple
# ejecutamos un BREAK

numero = 0

while(True):
    numero += 1
    if (numero == 3):
        continue
    print(f"Numero: {numero}")

    if(numero >= 8):
        break
