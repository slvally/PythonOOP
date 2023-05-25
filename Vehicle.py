# deklarasi kelas
class Vehicle:
    # deklarasi variabel
    __fuelType = ""
    __maxPassengers = 0
    __status = 0 
    # method dan konstruktor
    def __init__(self, fuelType ="", maxPassengers = 0):
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers
    #  get dans set semua variabel
    def setmaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers
    def getmaxPassengers(self):
        return self.__maxPassengers
    def setfuelType(self, fuelType):
        self.__fuelType = fuelType
    def getfuelType(self):
        return self.__fuelType
    def setstatus(self, status):
        self.__status = status
    def getstatus(self):
        if(self.__status == 0):
            return "inactive"
        elif(self.__status == 1):
            return "active"
        return self.__status
    # method move untuk mengubah status aktif/nonaktif
    def Move(self):
        if(self.__status == 0):
            self.__status = 1
        elif(self.__status == 1):
            self.__status = 0
