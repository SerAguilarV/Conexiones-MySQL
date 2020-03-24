import mysql.connector as Connect
import datetime

BaseD = "Banco"
Tabla = "Usuarios"

DB = Connect.connect(
    host = "192.168.1.104",
    user = "editor",
    password = "editorpass"
)

cursor = DB.cursor()
cursor.execute("Use Banco;")

#Add a day in the date when become an employee
# query = "Select ID, FECHA_INGRESO from Usuarios Where ID = 'S970359';"
# cursor.execute(query)
# for i in cursor:
#     print("ID: {}   Fecha Ingreso {}".format( i[0],i[1].strftime('%Y-%m-%d') ) )

# query2 = """
# Update Usuarios
# set FECHA_INGRESO = date_add(FECHA_INGRESO, interval 1 day)
# WHERE
# ID = 'S970359'
# """
# cursor.execute(query2)
# DB.commit()

# query = "Select ID, FECHA_INGRESO from Usuarios Where ID = 'S970359';"
# cursor.execute(query)
# for i in cursor:
#     print("ID: {}   Fecha Ingreso {}".format( i[0],i[1].strftime('%Y-%m-%d') ) )

#Add 1% at the salaries due the profits of the bank (Just for level 1 employees)
# query = """
# select ID, NIVEL, SUELDO from Usuarios where NIVEL = 1 and SUELDO >= 49000
# """
# cursor.execute(query)
# for i in cursor:
#     print("ID:{}   Nivel:{}   Salario:{}".format(
#         i[0], i[1], i[2]
#     ))

# query2 = """
# update Usuarios
# set SUELDO = SUELDO * 1.01
# where
# NIVEL = 1 and SUELDO >= 49000
# """
# cursor.execute(query2)
# cursor.execute(query)
# print('*'*30)
# for i in cursor:
#     print("ID:{}   Nivel:{}   Salario:{}".format(
#         i[0], i[1], i[2]
#     ))
# DB.commit()

#Update the salary for women with salary less than 12000. Add 5% at their salaries.
# query = """
# select U.ID, U.NIVEL, U.SUELDO, DU.GENERO
# from Usuarios U, Datos_Usuarios DU
# where DU.GENERO = 'M' and DU.ID = U.ID and U.SUELDO <= 12000
# """
# cursor.execute(query)
# for i in cursor:
#     print("ID:{}   Nivel:{}   Salario:{}   Genero:{}".format(
#         i[0], i[1], i[2], i[3]
#     ))

# query2 = """
# update Usuarios U, Datos_Usuarios DU
# set U.SUELDO = U.SUELDO * 1.05
# where
#     DU.ID = U.ID and
#     SUELDO <= 12000 and
#     DU.GENERO = 'M'
# """
# cursor.execute(query2)
# cursor.execute(query)
# print('*'*30)
# for i in cursor:
#     print("ID:{}   Nivel:{}   Salario:{}   Genero:{}".format(
#         i[0], i[1], i[2], i[3]
#     ))
# DB.commit()
