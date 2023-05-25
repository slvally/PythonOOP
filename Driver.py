from Person import Person

class Driver(Person):
    # deklarasi variabel
    __lisenceID = ""
    __activeUntil = ""
    __vehicleType = "" 
    # method dan konstruktor
    def __init__(self, lisenceID ="", activeUntil = "", vehicleType=""):
        self.__lisenceID = lisenceID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType
    #  get dans set semua variabel
    def setlisenceID(self, lisenceID):
        self.__lisenceID = lisenceID
    def getlisenceID(self):
        return self.__lisenceID
    def setactiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    def getactiveUntil(self):
        return self.__activeUntil
    def setvehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
    def getvehicleType(self):
        return self.__vehicleType
    # method untuk mengisi driver inherit person
    def setperdriver(self, NIK ="", Name = "", Gender="", lisenceID ="", activeUntil = "", vehicleType=""):
        self.__lisenceID=lisenceID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType
        self.setNIK(NIK)
        self.setName(Name)
        self.setGender(Gender)
    # method untuk menampilkan driver
    def printdriver(self):
        print("NIK: " + str(self.getNIK()))
        print("Name: " + str(self.getName()))
        print("Gender: " + str(self.getGender()))
        print("Lisence ID: " + str(self.getlisenceID()))
        print("Active Until: " + str(self.getactiveUntil()))
        print("Vehicle Type: " + str(self.getvehicleType()))
        print("Work Status: " + self.getSleep())