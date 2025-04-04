# Definición y equivalencia con las funciones estándar

def Saluda(nombre):
    print(f"Hola, me llamo {nombre}")

saludo = lambda nombre : print(f"Hola, me llamo {nombre}")

miNombre = "Borja"
Saluda(miNombre)
saludo(miNombre)
Saluda("Ana")
saludo("Ana")

#####################################################################

# Usamos las lambda para insertar lógica mediante parámetros

def Calcular(formula):
    for numero in range(1, 11, 1):
        print(f"Número: {numero} - Calculo: {formula(numero)}")


Calcular(lambda a: a * 5)
print("")

Calcular(lambda x: ((x * 5) - 10) / x)
print("")

formula1 = lambda x: x - (x * 0.75)
Calcular(formula1)
print("")

Calcular(lambda a: a % 2 == 0)
print("")