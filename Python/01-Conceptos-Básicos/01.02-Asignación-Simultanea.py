# Declaración de variables
a = 5
b = 10

# Intercambio sin asignación simultanea
temp = a
a = b
b = temp

print(f"Valor de A: {a}")
print(f"Valor de B: {b}")
print("")

#####################################################
a = 5
b = 10

# Intercambio sin asignación simultanea
a,b = b,a

print(f"Valor de A: {a}")
print(f"Valor de B: {b}")
print("")