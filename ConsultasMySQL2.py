import mysql.connector

BaseD = "Banco"
Tabla = "Usuarios"

DB = mysql.connector.connect(
    host = "192.168.1.104",
    user = "consultor",
    password = "consultorpass"
)

cursor = DB.cursor()
cursor.execute("Use Banco;")
cursor.execute("SET lc_time_names = 'es_MX';")

#********** Only uncomment the block to visualizate the result ************#

#QUERY for yougest and oldest person in the bank
# query = """
# SELECT * from Usuarios , Datos_Usuarios
# WHERE Usuarios.ID = Datos_Usuarios.ID
# ORDER BY Datos_Usuarios.FECHA_NACIMIENTO DESC
# LIMIT 1;"""
# cursor.execute(query)
# for i in cursor:
#     print("Datos de la persona mas joven: \n{}".format(i))

# query = """
# SELECT * from Usuarios , Datos_Usuarios
# WHERE Usuarios.ID = Datos_Usuarios.ID
# ORDER BY Datos_Usuarios.FECHA_NACIMIENTO
# LIMIT 1;"""
# cursor.execute(query)
# for i in cursor:
#     print("Datos de la persona mas vieja: \n{}".format(i))

#Query for getting the people whose born the same day and month
# query = """
# SELECT
#     CONCAT(
#         CAST(DAYOFMONTH(DU1.FECHA_NACIMIENTO) AS CHAR),
#         ' de ',
#         CAST(MONTHNAME(DU1.FECHA_NACIMIENTO) AS CHAR)
#     ) MES_DIA,
#     COUNT(*) CONTADOR
# FROM Datos_Usuarios DU1
# GROUP BY MES_DIA
# HAVING CONTADOR > 1
# ORDER BY CONTADOR DESC
# """
# cursor.execute(query)
# for i in cursor:
#     print("{} personas cumplen el {}".format(i[1], i[0]))

# Query for getting the average of salary according to Level
# query = """SELECT
#     U.NIVEL LEVEL,
#     AVG(U.SUELDO) AVERAGE_OF_SALARY
# FROM
#     Usuarios U
# GROUP BY
#     U.NIVEL
# """
# cursor.execute(query)
# for i in cursor:
#     print("Nivel {} : Promedio de Salario {}".format(i[0], i[1]))

#QUERY for getting the 5 people who has the maximum salary
# query = """
# SELECT
#     U.ID,
#     CONCAT(
#         DU.NOMBRE,
#         " ",
#         DU.APELLIDOS
#     ) 'Full Name',
#     U.NIVEL Level,
#     U.SUELDO Salary
# FROM
#     Usuarios U,
#     Datos_Usuarios DU
# WHERE
#     U.ID = DU.ID
# ORDER BY
#     U.SUELDO DESC
# LIMIT 5;"""
# cursor.execute(query)
# print("Datos de las 5 persona con el mayor sueldo:")
# for i in cursor:
#     print("{}".format(i))

# QUERY for getting the 5 people who has the maximum salary
# query = """
# SELECT
#     U.ID,
#     CONCAT(
#         DU.NOMBRE,
#         " ",
#         DU.APELLIDOS
#     ) 'Full Name',
#     U.NIVEL Level,
#     U.SUELDO Salary
# FROM
#     Usuarios U,
#     Datos_Usuarios DU
# WHERE
#     U.ID = DU.ID
# ORDER BY
#     U.SUELDO DESC
# LIMIT 5;"""
# cursor.execute(query)
# print("Datos de las 5 persona con el mayor sueldo:")
# for i in cursor:
#     print("{}".format(i))

#QUERY for getting the person who has the maximum salary per level
# query = """
# SELECT
#     U.NIVEL Level,
#     U.ID,
#     CONCAT(
#         DU.NOMBRE,
#         " ",
#         DU.APELLIDOS
#     ) 'Full Name',
#     MAX(U.SUELDO) Salary
# FROM
#     Usuarios U,
#     Datos_Usuarios DU
# WHERE
#     U.ID = DU.ID
# Group BY U.NIVEL
# """
# cursor.execute(query)
# print("Datos de las 5 persona con el mayor sueldo:")
# for i in cursor:
#     print("{}".format(i))

