# Web Scraping Lista de Nombres
import json
from urllib.request import urlopen

class Lista_Scraping():
    def __init__(self):
        self.URL_Nombres_H = "http://datamx.io/api/action/datastore_search_sql?sql=SELECT%20*%20from%20%22df9d4714-a5a3-469f-ae9a-d4c28b34d954%22%20"
        self.URL_Nombres_M = "http://datamx.io/api/action/datastore_search_sql?sql=SELECT%20*%20from%20%228047ffa2-dac3-4675-87e1-e7eb4de09825%22%20"
        self.URL_Apellidos = "http://datamx.io/api/action/datastore_search_sql?sql=SELECT%20*%20from%20%2256f84bf5-8255-4b15-949d-912fc79477ce%22%20"
        self.VectorNombresH, self.VectorProbaH = self.VectorNombresProbabilidades(Base="H")
        self.VectorNombresM, self.VectorProbaM = self.VectorNombresProbabilidades(Base="M")
        self.VectorApellidos, self.VectorProbaApellido1, self.VectorProbaApellido2 = self.VectorApellidosProbabilidades()

    def VectorApellidosProbabilidades(self):
        parse = json.loads(urlopen(self.URL_Apellidos).read())
        Nombres = []
        Frecuencias1 = []
        Frecuencias2 = []
        for Nombre in parse["result"]["records"]:
            Nombres.append(Nombre["apellido"].title())
            Frecuencias1.append(int(Nombre["frec_pri"]))
            Frecuencias2.append(int(Nombre["frec_seg"]))
        VFrec1 = Frecuencias1
        VFrec2 = Frecuencias2
        return Nombres, VFrec1, VFrec2

    def VectorNombresProbabilidades(self, Base = ""):
        if Base == "M":
            url = self.URL_Nombres_M
            index = "nombre"
        else:
            url = self.URL_Nombres_H
            index = "nombre"
        parse = json.loads(urlopen(url).read())
        Nombres = []
        Frecuencias = []
        for Nombre in parse["result"]["records"]:
            Nombres.append(Nombre[index].title())
            Frecuencias.append(int(Nombre["frec"]))
        VFrec = Frecuencias
        return Nombres, VFrec

    def getListasNombresHombre(self):
        return self.VectorNombresH, self.VectorProbaH

    def getListasNombresMujer(self):
        return self.VectorNombresM, self.VectorProbaM

    def getListasApellidos(self):
        return self.VectorApellidos, self.VectorProbaApellido1, self.VectorProbaApellido2

# Lista = Lista_Scraping()
# VH, VPH = Lista.getListasNombresHombre()
# print(VH[0:5], VPH[0:5])

# VM, VPM = Lista.getListasNombresMujer()
# print(VM[0:5], VPM[0:5])

# VA, VPA1, VPA2 = Lista.getListasApellidos()
# print(VA[0:5], VPA1[0:5], VPA2[0:5])

