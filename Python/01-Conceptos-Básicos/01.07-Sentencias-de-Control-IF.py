# Declaración de variables
a = 330
b = 33

if(b > a):
    print(f"B es mayor de A. Valor de B: {b}")
elif(a > b):
    print(f"A es mayor de B. Valor de A: {a}")
else:
    print(f"A es igual a B")

print("Finalizado el IF/ELSE")
print("")

if(b > a):
    print(f"B es mayor de A. Valor de B: {b}")
elif(a > b):
    print(f"A es mayor de B. Valor de A: {a}")
elif(a == b):
    print(f"A es igual a B")

print("Finalizado el IF/ELSE")
print("")

if(b > a):
    print(f"B es mayor de A. Valor de B: {b}")
else:
    if(a > b):
        print(f"A es mayor de B. Valor de A: {a}")
    else:
        print(f"A es igual a B")

print("Finalizado el IF/ELSE")
print("")