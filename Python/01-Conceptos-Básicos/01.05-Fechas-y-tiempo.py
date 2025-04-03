# Importamos módulos
from datetime import datetime
import time
import locale, pytz

# Configuración regional
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Declaración de variables
dt1 = datetime.now().date()
dt2 = datetime.now()

print(f"Fecha 1: {dt1}")
print(f"Fecha 2: {dt2}")

print(f"Día: {dt2.day}")
print(f"Día: {str(dt2.day).zfill(2)}")
print(f"Mes: {dt2.month}")
print(f"Mes: {str(dt2.month).zfill(2)}")
print(f"Año: {dt2.year}")
print(f"Hora: {dt2.hour}")
print(f"Minutos: {dt2.minute}")
print(f"Segundos: {dt2.second}")
print(f"Milisegundos: {dt2.microsecond} \n")

# Convertir texto en fecha
fecha = input("Escribe una fecha (dd-mm-yyyy): ")
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()
print(f"Fecha: {dt3}")
dt3 = datetime.strptime(fecha, "%d-%m-%Y")
print(f"Fecha: {dt3}")

print(f"Hoy es {dt3.strftime("%A, %d de %B de %Y")} \n")

# Calculo con fechas
dtr = dt2 - dt3             # Resultado un TIMEDELTA
print(dtr)
print(dtr.days)
print(dtr.seconds)
print(dtr.microseconds)

print(dtr.total_seconds())

print(f"Edad: {dtr.days / 365}")

edad = divmod(dtr.days, 365)
print(edad)
print(f"Tienes {edad[0]} años y {edad[1]} días")
