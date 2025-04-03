# Declaración de variables
citricos = ["narajan", "limón", "pomelo", "líma", "mandarina"]

for fruta in citricos:
    print(f"-> {fruta}")
print("")

for index in range(len(citricos)):
    print(f"{index} -> {citricos[index]}")
print("")

for index, fruta in enumerate(citricos):
    print(f"{index} -> {fruta}")
print("")

for fruta in citricos:
    if(fruta == "pomelo"):
        print(f"-> BREAK <-")
        break
    print(f"-> {fruta}")
print("")

for fruta in citricos:
    if(fruta == "pomelo"):
        print(f"-> CONTINUE <-")
        continue
    print(f"-> {fruta}")
print("")


# del 0 a 4
for numero in range(5):
    print(f"Número: {numero}")
print("")    

# del 10 al 20 de 2 en 2
for numero in range(10, 21, 2):
    print(f"Número: {numero}")
print("")   

# del 20 al 5 de -3 en -3
for numero in range(20, 4, -3):
    print(f"Número: {numero}")
print("")   