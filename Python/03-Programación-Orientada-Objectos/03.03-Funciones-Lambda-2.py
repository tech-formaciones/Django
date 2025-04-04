# Uso de funciones lambda con funciones para manejar los datos de las colecciones

numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8, 22, 1012]

def MayorDeCien(lista):
    resultado = []

    for numero in lista:
        if(numero > 100):
            resultado.append(numero)

    return resultado

print(f"Números mayores de 100 - Función Estándar: {MayorDeCien(numeros)}")
print("")

###########################################################################

def NumMayorCien(numero):
    if(numero > 100):
        return True
    else:
        return False
    
print(f"Números mayores de 100 - FILTER + Función Estándar: {list(filter(NumMayorCien, numeros))}")
print("")

###########################################################################

print(f"Números mayores de 100 - FILTER + Función Lambda: {list(filter(lambda x: x > 100, numeros))}")
print(f"Números pares - FILTER + Función Lambda: {list(filter(lambda x: x % 2 == 0, numeros))}")
print("")

###########################################################################

print(f"Numeros: {numeros}")
resultado = list(map(lambda x: (x + 10) / 2, numeros))
print(f"Resultado de sumar 10 y dividir entre 2: {resultado}")
print("")

print(f"Suma Total: {sum(numeros)}")
print(f"Suma Pares: {sum(filter(lambda h: h % 2 == 0, numeros))}")
#print(f"Resultado: {reduce(lambda x, y: x + y, numeros)}")
print("")

print(f"Algún numero es par ???: {any(map(lambda x: x % 2 == 0, numeros))}")
print(f"Algún numero es par ???: {any(x % 2 == 0 for x in numeros)}")
print("")

print(f"Todos los numeros son par ???: {all(map(lambda x: x % 2 == 0, numeros))}")
print(f"Todos los numeros son par ???: {all(x % 2 == 0 for x in numeros)}")
print("")