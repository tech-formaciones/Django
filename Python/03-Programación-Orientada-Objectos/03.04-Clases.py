# Definición de una clase

class Alumno:
    """Clase demo curso Python + Django"""

    # Variables de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaMatricula = None

    # Función constructora, se ejecuta al instanciar el objeto.
    def __init__(self) -> None:
        pass

    def __init__(self, nombre, apellido1, apellido2) -> None:
        self.Nombre = nombre
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2

    def getNombreCompleto(self) -> str:
        """Retorna el nombre completo del Alumno"""
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"
    

# Herencia

class Estudiante(Alumno):
    """Clase Estudiante que hereda de Alumno"""

    # Variables
    Curso = None

    # Sobreescribimos el constructor
    def __init__(self, nombre, apellido1, apellido2, curso) -> None:
        super().__init__(nombre, apellido1, apellido2)
        
        self.Curso = curso

    # Sobreescribimos getNombreCompleto
    def getNombreCompleto(self) -> str:
        return f"{super().getNombreCompleto()} - Curos: {self.Curso}"
    
    # Añadir nuevas funciones
    def newFuctionDemo(self) -> str:
        return "demo"
    

# Instaciamos y usamos los objetos
alumno = Alumno("Ana", "Sanz", "Rozas")
alumno.Nombre = "Carlos"
print(alumno.Nombre)
print(alumno.getNombreCompleto())
print("")


estudiante = Estudiante("Ana", "Sanz", "Rozas", "2B")
estudiante.Nombre = "Carlos"
print(estudiante.Nombre)
print(estudiante.getNombreCompleto())