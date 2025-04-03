# Declaración de variables
numero1 = 0
numero2 = 100

try:
    try:
        file = open("fichero.txt")
        numero = numero2 / numero1
    except ZeroDivisionError as err:
        print(f"-> {err}")
        print(f"-> {type(err)}")
        print(f"Error al dividir por cero")
        raise
        raise Exception("Error al dividir por cero")
    except FileNotFoundError as err:
        raise
    except Exception as err:
        print(f"-> {err}")
        print(f"Se ha producido un error")
    finally:
        print(f"Sentencia Final")
except Exception as err:
    print(f"-> {err}")
    print(f"-> {type(err)}")
    print(f"Try Superior")