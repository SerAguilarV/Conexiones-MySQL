import mysql.connector as Connect

BaseD = "Banco"
Tabla = "Datos_Usuarios"

DB = Connect.connect(
    host = "192.168.1.104",
    user = "cel_sergio",
    password = "Saav260230"
)

cursor = DB.cursor()

# Mostrar Tablas
print('\n' + '*'*15 + "Bases de Datos en el SERVIDOR" + '*'*15 )
cursor.execute("SHOW DATABASES;")
for i in cursor:
    print("Base: {}".format(i[0]))

# Seleccionar una Base de Datos y mostrar Tablas
print('\n' + '*'*15 + "Tablas en Base Seleccionada" + '*'*15 )
cursor.execute("USE " + BaseD)
cursor.execute(" SHOW TABLES")
for i in cursor:
    print("Tabla: {}".format(i[0]))

# Numero de Registros en Tabla Seleccionada
print('\n' + '*'*15 + "Numero de Registros" + '*'*15 )
cursor.execute("SELECT COUNT(*) FROM " + Tabla)
for i in cursor:
    print("Número de Registros: {}".format(i[0]))

# Informacion de la tabla
print('\n' + '*'*15 + "Informacion de Tabla {}".format(Tabla) + '*'*15 )
cursor.execute("DESCRIBE " + Tabla)
info = ("Field", "Type", "Null", "Key", "Default", "Extra")
txt = ""
for cont1, i in enumerate(cursor):
    for cont2, tipo_val in enumerate(i):
        txt = txt + info[cont2] + " : " + str(tipo_val) + "    "
    print("Columna {} : ".format(cont1 +1) + txt)
    txt =  ""

# Mostrar INDEX de Tabla
print('\n' + '*'*15 + "Mostrar Index de tabla " + Tabla + '*'*15 )
cursor.execute("SHOW INDEX FROM " + Tabla)
for i in cursor:
    print("INDEX: {}".format(i))

# Todos los registros de la Tabla
print('\n' + '*'*15 + "Todos los registros de tabla " + Tabla + '*'*15 )
cursor.execute("SELECT * FROM " + Tabla + " ORDER BY NIVEL")
for cont, i in enumerate(cursor):
    print(str(cont+1) + ": {}".format(i))



DB.close()