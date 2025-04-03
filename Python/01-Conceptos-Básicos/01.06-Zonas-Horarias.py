# Importamos módulos
from datetime import datetime
import pytz

# Mostrar las zonas horarias
print(pytz.all_timezones)
print("")

# Sin Zona Hoararía
dt = datetime.now()
print(f"Fecha: {dt}")
print(f"Zona Horaría: {dt.tzinfo}")
print("")

# Con Zona Hoararía
dtQatar = datetime.now(pytz.timezone("Asia/Qatar"))
print(f"Fecha: {dtQatar}")
print(f"Zona Horaría: {dtQatar.tzinfo}")
print("")

print(f"Fecha Tokyo: {datetime.now(pytz.timezone("Asia/Tokyo"))}")
print(f"Fecha Madrid: {datetime.now(pytz.timezone("Europe/Madrid"))}")
print(f"Fecha New York: {datetime.now(pytz.timezone("America/New_York"))}")
print(f"Fecha GMT -12: {datetime.now(pytz.timezone("Etc/GMT-12"))}")
