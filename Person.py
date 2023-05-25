class Person:
    # deklarasi variabel
    __NIK = ""
    __Name = ""
    __Gender = "" 
    __Sleep = 0
    # method dan konstruktor
    def __init__(self, NIK ="", Name = "", Gender=""):
        self.__NIK = NIK
        self.__Name = Name
        self.__Gender = Gender
    #  get dans set semua variabel
    def setNIK(self, NIK):
        self.__NIK = NIK
    def getNIK(self):
        return self.__NIK
    def setName(self, Name):
        self.__Name = Name
    def getName(self):
        return self.__Name
    def setGender(self, Gender):
        self.__Gender = Gender
    def getGender(self):
        return self.__Gender
    def setSleep(self, Sleep):
        self.__Sleep = Sleep
    def getSleep(self):
        if(self.__Sleep == 0):
            return "sleeping"
        elif(self.__Sleep == 1):
            return "working"
        return self.__status
    # method untuk mengubah status person sleep/tidak
    def sleep(self):
        if(self.__Sleep == 0):
            self.__Sleep = 1
        elif(self.__Sleep == 1):
            self.__Sleep = 0

