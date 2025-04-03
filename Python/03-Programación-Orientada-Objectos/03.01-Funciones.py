from datetime import datetime

def func1():
    """func1, no tiene parámetros y no retorna datos"""
    print("Hola Mundo !!!")

def func2(nombre, numero):
    """func2, tiene parámetros y no retorna datos"""
    print(f"Me llamo {nombre} y mi número de la suerte es {numero}")

def func3(frase):
    """func1, tiene parámetros y retorna datos"""
    return len(frase)

def func4():
    """func1, no tiene parámetros y retorna datos"""
    return datetime.now().date().strftime("%A")

# Ejecutar funciones
func1()
func2("Borja", 12)
cantidad = func3("En un lugar de la mancha de cuyo ....")
print(f"Cantidad: {cantidad}")
print(f"Día de la semana: {func4()}")
print("")

# Ejemplos sobre parámetros
def resta1(a, b):
    return a - b

print(f"85 - 10 = {resta1(85, 10)}")        # por posición
print(f"85 - 10 = {resta1(a=85, b=10)}")    # por posición y nombre
print(f"85 - 10 = {resta1(b=10, a=85)}")    # por nombre
print("")

def resta2(a, b=10):
    return a - b

print(f"85 - 10 = {resta2(85, 10)}")        # por posición
print(f"85 - 10 = {resta2(a=85, b=10)}")    # por posición y nombre
print(f"85 - 10 = {resta2(b=10, a=85)}")    # por nombre
print(f"85 - 10 = {resta2(85)}")            # por posición, solo el obligatorio
print(f"85 - 10 = {resta2(a=85)}")          # por nombre, solo el obligatorio
print("")


def resta3(a=85, b=10):
    return a - b

print(f"85 - 10 = {resta3(85, 10)}")        # por posición
print(f"85 - 10 = {resta3(a=85, b=10)}")    # por posición y nombre
print(f"85 - 10 = {resta3(b=10, a=85)}")    # por nombre
print(f"85 - 10 = {resta3(85)}")            # por posición
print(f"85 - 10 = {resta3(a=85)}")          # por nombre
print(f"85 - 10 = {resta3(b=10)}")          # por nombre
print(f"85 - 10 = {resta3())}")              # sin valores para los parámetros
print("")


# Número de parámetros indeterminados
def test(*args):
    for arg in args:
        print(f"-> {arg}")
    print("")
    
test()
test(10, 20, 30)
test("hola")
test("hola", 10, [10,30,15])