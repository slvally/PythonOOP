from Vehicle import Vehicle

class Airplane(Vehicle):
    # deklarasi variabel
    __age = ""
    __type = ""
    __wingsLength = "" 
    # method dan konstruktor
    def __init__(self, age ="", type = "", wingsLength=""):
        self.__age = age
        self.__type = type
        self.__wingsLength = wingsLength
    #  get dans set semua variabel
    def setage(self, age):
        self.__age = age
    def getage(self):
        return self.__age
    def settype(self, type):
        self.__type = type
    def gettype(self):
        return self.__type
    def setwingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
    def getwingsLength(self):
        return self.__wingsLength
    # method untuk mengisi airplane inherit vehicle
    def setvecplane(self, fuelType ="", maxPassengers = 0, age ="", type = "", wingsLength=""):
        self.__age=age
        self.__type = type
        self.__wingsLength = wingsLength
        self.setfuelType(fuelType)
        self.setmaxPassengers(maxPassengers)
    # method untuk print airplane
    def printplane(self):
        print("Type: " + str(self.gettype()))
        print("Age: " + str(self.getage()))
        print("wingsLength: " + str(self.getwingsLength()))
        print("FuelType: " + str(self.getfuelType()))
        print("Max Passengers: " + str(self.getmaxPassengers()))
        print("Airplane Status: " + self.getstatus())