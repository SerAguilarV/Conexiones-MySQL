import mysql.connector
from Rellenado_Fake_DB import Usuario_Fake, Datos_Usuario_Fake
from WebScraping_NombresApellidos import Lista_Scraping

BaseD = "Banco"
Tabla = "Usuarios"

DB = mysql.connector.connect(
    host = "192.168.1.104",
    user = "editor",
    password = "editorpass"
)

cursor = DB.cursor()
cursor.execute("Use Banco")

#*********Insert INTO Usuarios*********#
# sql = "INSERT INTO Usuarios (ID, FECHA_INGRESO, NIVEL, SUELDO) VALUES (%s, %s, %s, %s)"
# values = []
# for i in range(500):
#     User = Rellenado_Fake_DB.Usuario_Fake()
#     values.append((User.ID, User.FECHA_INGRESO, User.NIVEL, User.SUELDO))
# cursor.executemany(sql, values)
# DB.commit()
# print(cursor.rowcount, " Registros Insertados")

#*********Insert Into DatosMexico*********#
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

#*********Base Nombres Mujeres*********#
# sql = "INSERT INTO Nombres_M(NOMBRE, FRECUENCIA) VALUES (%s, %s)"
# values = [(VM[ind], VPM[ind])  for ind, val in enumerate(VM) ]
# cursor.executemany(sql, values)
# print(cursor.rowcount, " Registros Insertados en base Mujeres")
# #DB.commit()

#*********Base Apellidos*********#
# sql = "INSERT INTO Apellidos(APELLIDO, FRECUENCIA_PRIMERO, FRECUENCIA_SEGUNDO) VALUES (%s, %s, %s)"
# values = [(VA[ind], VPA1[ind], VPA2[ind],)  for ind, val in enumerate(VA) ]
# cursor.executemany(sql, values)
# print(cursor.rowcount, " Registros Insertados en base Apellidos")
# DB.commit()

#*********Insertar en Datos Usuarios*********#
# Values = []
# cursor.execute("SELECT ID from Usuarios;")
# Datos = Datos_Usuario_Fake()
# Ids = [i for i in cursor]
# for i in Ids:
#     id_s = i[0]
#     Datos.NuevosDatos(id_s)
#     Values.append((str(id_s), str(Datos.NOMBRE), str(Datos.APELLIDOS), str(Datos.GENERO), str(Datos.FECHA_NAC)))
# cursor.execute("Use Banco;")
# sql = """INSERT INTO Datos_Usuarios(ID, NOMBRE, APELLIDOS, GENERO, FECHA_NACIMIENTO) 
#         VALUES ((SELECT ID FROM Usuarios WHERE ID = %s), %s, %s, %s, %s) """
# vals = Values
# cursor.executemany(sql, vals)
# print("Insertados {}".format(cursor.rowcount))
# DB.commit()
