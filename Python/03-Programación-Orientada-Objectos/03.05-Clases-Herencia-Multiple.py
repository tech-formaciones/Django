class A:
    Numero1 = 0
    Numero2 = 0

    def Suma(self) -> int:
        return self.Numero1 + self.Numero2
    
    def Resta(self) -> int:
        return self.Numero1 - self.Numero2
    
class B:
    Numero1 = 0
    Numero2 = 0

    def Suma(self) -> int:
        return f"B > {self.Numero1 + self.Numero2}"

    def Multiplica(self) -> int:
        return self.Numero1 * self.Numero2
    
    def Divide(self) -> int:
        return self.Numero1 / self.Numero2

# Cuando el nombre de las funciones coinciden, solo se hereda la función de la clase
# más a las izquierda (la espeficada en primer lugar).

# Cuando el nombre de las varioables coinciden, son únicas y se utilizan los valores
# con las funciones de las diferentes clases.

class C(A, B): pass

c = C()
c.Numero1 = 20
c.Numero2 = 16
print(f"-> {c.Suma()}")
print(f"-> {c.Resta()}")
print(f"-> {c.Multiplica()}")
print(f"-> {c.Divide()}")