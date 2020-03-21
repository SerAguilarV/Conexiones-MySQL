#random numero de usuario, fecha, edad, nivel, sueldo
import random
import datetime
import numpy as np
import mysql.connector
# Distribucion
# 5% Nivel 1
# 15% Nivel 2
# 35% Nivel 3
# 45% Nuivel 4

#   Sueldos
# Nivel 1  50,0000 - 35,000
# Nivel 2  40,0000 - 22,000
# Nivel 3  25,0000 - 18,000
# Nivel 4  20,0000 - 10,000


class Usuario_Fake:
    def __init__(self):
        self.Niveles = [1,2,3,4]
        self.Distribucion = [0.05, .15, .35, .45]
        self.Sueldos = {"N1" : (50000, 35000), "N2":(40000, 22000),
                        "N3":(25000, 18000), "N4": (20000, 10000)}
        self.ID = self.getID()
        self.FECHA_INGRESO = self.getFechaIngreso()
        self.NIVEL = self.getNivel()
        self.SUELDO = self.getSueldo()

    def __str__(self):
        return "ID: {}\nFecha de Ingreso: {}\nNivel: {}\nSueldo: {}".format(
                self.ID, self.FECHA_INGRESO, self.NIVEL, self.SUELDO
        )

    def getID(self):
        num = str(random.randint(1,999999))
        if len(num)<6:
            num = "0"*(6-len(num)) + str(num)
        return "S"+num

    def getFechaIngreso(self):
        fecha = datetime.datetime.now() - datetime.timedelta(days = random.randint(1, 30*365))
        return fecha.strftime("%Y-%m-%d")

    def getNivel(self):
        return int(np.random.choice(self.Niveles, 1, p = self.Distribucion)[0])

    def getSueldo(self):
        Nivel = "N" + str(self.NIVEL)
        RangoSup, RangoInf = self.Sueldos[Nivel]
        return random.randint(RangoInf/100 , RangoSup/100)*100

class Datos_Usuario_Fake:
    def __init__(self):
        self.ID = ""
        self.GENERO = ""
        self.NOMBRE = ""
        self.APELLIDOS = ""
        self.EDAD = ""
        self.myDB = mysql.connector.connect(
            host = "192.168.1.104",
            user = "cel_sergio",
            password = "Saav260230"
        )
        self.cursor = self.myDB.cursor()
        self.VH, self.VPH = self.GetVectoresNombre("H")
        self.VM, self.VPM = self.GetVectoresNombre("M")
        self.VA, self.VPA1, self.VPA2 = self.GetVectoresApellidos()

    def GetVectoresNombre(self, Base):
        if Base == "H":
            DB = "Nombres_H"
        else:
            DB = "Nombres_M"
        query = "USE DatosMexico"
        self.cursor.execute(query)
        query = "SELECT NOMBRE, FRECUENCIA FROM {} ".format(DB)
        self.cursor.execute(query)
        VN = []
        VP = []
        for i in self.cursor:
            VN.append(i[0])
            VP.append(i[1])
        VP = [i/sum(VP) for i in VP]
        return VN, VP

    def GetVectoresApellidos(self):
        query = "SELECT APELLIDO, FRECUENCIA_PRIMERO, FRECUENCIA_SEGUNDO FROM {} ".format("Apellidos")
        self.cursor.execute(query)
        VN = []
        VP1 = []
        VP2 = []
        for i in self.cursor:
            VN.append(i[0])
            VP1.append(i[1])
            VP2.append(i[2])
        VP1 = [i/sum(VP1) for i in VP1]
        VP2 = [i/sum(VP2) for i in VP2]
        return VN, VP1, VP2

    def NuevosDatos(self, ID):
        self.ID = ID
        self.GENERO = self.getGENERO()
        self.NOMBRE = self.getNOMBRE()
        self.APELLIDOS = self.getAPELLIDOS()
        self.FECHA_NAC = self.getFECHAN()

    def getGENERO(self):
        if random.randint(0,1) == 1:
            return "M"
        return "H"

    def getNOMBRE(self):
        pass
        if self.GENERO == "M":
            return np.random.choice(self.VM, 1, p = self.VPM)[0]
        else:
            return np.random.choice(self.VH, 1, p = self.VPH)[0]

    def getAPELLIDOS(self):
        self.VA, self.VPA1, self.VPA2
        A1 = np.random.choice(self.VA, 1, p = self.VPA1)[0]
        A2 = np.random.choice(self.VA, 1, p = self.VPA2)[0]
        return A1 + " " + A2

    def getFECHAN(self):
        query = "Use Banco;"
        self.cursor.execute(query)
        query = "SELECT FECHA_INGRESO from Usuarios WHERE ID = '{}';".format(self.ID)
        self.cursor.execute(query)
        Fecha = ""
        for F in self.cursor:
            Fecha = F
        Fecha = Fecha[0]
        RandAñoNacimiento = random.randint(abs(datetime.datetime.now().year - Fecha.year) + 20, 60)
        AñosDiff2 = datetime.datetime.now() - datetime.timedelta(
                days = RandAñoNacimiento * (365.25))
        FechaFake = datetime.datetime(
            AñosDiff2.year, 1, 1, 0, 0) + datetime.timedelta(
                days = random.randint(0,366)
                )
        return FechaFake.strftime('%Y-%m-%d %H:%M:%S')
        #Fecha de ingreso - 20 años
        # diferencia entre (Fecha de ingreso - 20 años)
        # randint este valor hasta (60)

# Usuario = Usuario_Fake()
# print(Usuario)

Values = []
myDB = mysql.connector.connect(
    host = "192.168.1.104",
    user = "cel_sergio",
    password = "Saav260230"
)

cursor = myDB.cursor()
cursos2  =  myDB.cursor()
cursor.execute("Use Banco;")

cursor.execute("SELECT ID from Usuarios;")
Datos = Datos_Usuario_Fake()
Ids = [i for i in cursor]
for i in Ids:
    id_s = i[0]
    Datos.NuevosDatos(id_s)
    Values.append((str(id_s), str(Datos.NOMBRE), str(Datos.APELLIDOS), str(Datos.GENERO), str(Datos.FECHA_NAC)))
cursor.execute("Use Banco;")
sql = """INSERT INTO Datos_Usuarios(ID, NOMBRE, APELLIDOS, GENERO, FECHA_NACIMIENTO) 
        VALUES ((SELECT ID FROM Usuarios WHERE ID = %s), %s, %s, %s, %s) """
vals = Values
print(Values[0])
pass
cursor.executemany(sql, vals)
print("Insertados {}".format(cursor.rowcount))
myDB.commit()