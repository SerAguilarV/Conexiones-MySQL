import datetime
import random

Fecha = datetime.datetime(1995, 1, 12, 0, 0)
RandAñoNacimiento = random.randint(abs(datetime.datetime.now().year - Fecha.year) + 20, 60)
AñosDiff2 = datetime.datetime.now() - datetime.timedelta(days = RandAñoNacimiento * (365.25))
FechaFake = datetime.datetime(AñosDiff2.year, 1, 1, 0, 0) + datetime.timedelta(days = random.randint(0,366))
print(FechaFake)