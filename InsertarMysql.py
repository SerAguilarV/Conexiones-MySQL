import mysql.connector
import Rellenado_Fake_DB
from WebScraping_NombresApellidos import Lista_Scraping

BaseD = "Banco"
Tabla = "Usuarios"

DB = mysql.connector.connect(
    host = "192.168.1.104",
    user = "cel_sergio",
    password = "Saav260230"
)

cursor = DB.cursor()
cursor.execute("Use Banco")

## Insert INTO Usuarios
# sql = "INSERT INTO Usuarios (ID, FECHA_INGRESO, NIVEL, SUELDO) VALUES (%s, %s, %s, %s)"
# values = []
# for i in range(500):
#     User = Rellenado_Fake_DB.Usuario_Fake()
#     values.append((User.ID, User.FECHA_INGRESO, User.NIVEL, User.SUELDO))
# cursor.executemany(sql, values)
# DB.commit()
# print(cursor.rowcount, " Registros Insertados")

### Insert Into DatosMexico
# Lista = Lista_Scraping()
# VH, VPH = Lista.getListasNombresHombre()
# print(VH[0:5], VPH[0:5])
# VM, VPM = Lista.getListasNombresMujer()
# print(VM[0:5], VPM[0:5])
# VA, VPA1, VPA2 = Lista.getListasApellidos()
# print(VA[0:5], VPA1[0:5], VPA2[0:5])
# # Base Nombres Hombres
# sql = "INSERT INTO Nombres_H(NOMBRE, FRECUENCIA) VALUES (%s, %s)"
# values = [(VH[ind], VPH[ind])  for ind, val in enumerate(VH) ]
# cursor.executemany(sql, values)
# print(cursor.rowcount, " Registros Insertados en base Hombres")
# #DB.commit()

# # Base Nombres Mujeres
# sql = "INSERT INTO Nombres_M(NOMBRE, FRECUENCIA) VALUES (%s, %s)"
# values = [(VM[ind], VPM[ind])  for ind, val in enumerate(VM) ]
# cursor.executemany(sql, values)
# print(cursor.rowcount, " Registros Insertados en base Mujeres")
# #DB.commit()

# # Base Apellidos
# sql = "INSERT INTO Apellidos(APELLIDO, FRECUENCIA_PRIMERO, FRECUENCIA_SEGUNDO) VALUES (%s, %s, %s)"
# values = [(VA[ind], VPA1[ind], VPA2[ind],)  for ind, val in enumerate(VA) ]
# cursor.executemany(sql, values)
# print(cursor.rowcount, " Registros Insertados en base Apellidos")
# DB.commit()


#Insert INTO Datos_Usuarios
sql = "SELECT ID FROM Usuarios"
cursor.execute(sql)
IDs = [i for i in cursor]



sql = """INSERT INTO Datos_Usuarios (ID, NOMBRE, APELLIDOS, GENERO) 
        VALUES ( (SELECT ID FROM Usuarios WHERE ID = %s), %s, %s, %s)"""
values = []
for i in range(500):
    User = Rellenado_Fake_DB.Usuario_Fake()
    values.append((User.ID, User.FECHA_INGRESO, User.NIVEL, User.SUELDO))
cursor.executemany(sql, values)
DB.commit()
print(cursor.rowcount, " Registros Insertados")
