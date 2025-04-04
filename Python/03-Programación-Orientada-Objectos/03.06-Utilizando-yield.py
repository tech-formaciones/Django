# Definición de variables

numeros = [1, 85, 200, 15, 152, -450, 5, 3061, 63, 77, 8, 22, 1012]
print(f" Datos: {numeros}")

def func1(datos):
    for i in datos:
        return i * 5
    
def func2(datos):
    resultado = []

    for i in datos:
        resultado.append(i * 5)

    return resultado
    
print(f" Func1: {func1(numeros)}")
print(f" Func2: {func2(numeros)}")
print(f"Lambda: {list(map(lambda x: x * 5, numeros))}")


def func3(datos):
    for i in datos:
        yield i * 5

print(f" Func3: {func3(numeros)}")
print(f" Func3 + To List: {list(func3(numeros))}")

generador = func3(numeros)
print(f" -> {next(generador)}")
print(f" -> {next(generador)}")
print(f" -> {next(generador)}")
print(f" -> {next(generador)}")
print(f" -> {next(generador)}")
print("")

generador = func3(numeros)
for i in generador:
    print(f" >> {i}")
print("")


try:
    generador = func3(numeros)

    for i in range(20):
        print(f" --> {next(generador)}")

except StopIteration as err:
    print(f"Error: {err}")