# deklarasi kelas
from Vehicle import Vehicle

class Ship(Vehicle):
    # deklarasi variabel
    __age = ""
    __type = ""
    __countryOfManufacture = "" 
    # method dan konstruktor
    def __init__(self, age ="", type = "", countryOfManufacture=""):
        self.__age = age
        self.__type = type
        self.__countryOfManufacture = countryOfManufacture
    #  get dans set semua variabel
    def setage(self, age):
        self.__age = age
    def getage(self):
        return self.__age
    def settype(self, type):
        self.__type = type
    def gettype(self):
        return self.__type
    def setcountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
    def getcountryOfManufacture(self):
        return self.__countryOfManufacture
    # method untuk mengisi ship inherit dari vehicle
    def setvecship(self, fuelType ="", maxPassengers = 0, age ="", type = "", countryOfManufacture=""):
        self.__age=age
        self.__type = type
        self.__countryOfManufacture = countryOfManufacture
        self.setfuelType(fuelType)
        self.setmaxPassengers(maxPassengers)
    # method untuk print ship
    def printship(self):
        print("Type: " + str(self.gettype()))
        print("Age: " + str(self.getage()))
        print("Country: " + str(self.getcountryOfManufacture()))
        print("FuelType: " + str(self.getfuelType()))
        print("Max Passengers: " + str(self.getmaxPassengers()))
        print("Ship Status: " + self.getstatus())