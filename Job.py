from Person import Person

class Job(Person):
    # deklarasi variabel
    __NIP = ""
    __companyName = ""
    __position = "" 
    # method dan konstruktor
    def __init__(self, NIP ="", companyName = "", position=""):
        self.__NIP = NIP
        self.__companyName = companyName
        self.__position = position
    #  get dans set semua variabel
    def setNIP(self, NIP):
        self.__NIP = NIP
    def getNIP(self):
        return self.__NIP
    def setcompanyName(self, companyName):
        self.__companyName = companyName
    def getcompanyName(self):
        return self.__companyName
    def setposition(self, position):
        self.__position = position
    def getposition(self):
        return self.__position
    # method untuk mengisi job inherit person
    def setperjob(self, NIK ="", Name = "", Gender="", NIP ="", companyName = "", position=""):
        self.__NIP=NIP
        self.__companyName = companyName
        self.__position = position
        self.setNIK(NIK)
        self.setName(Name)
        self.setGender(Gender)
    # method untuk menampilkan job
    def printjob(self):
        print("NIK: " + str(self.getNIK()))
        print("Name: " + str(self.getName()))
        print("Gender: " + str(self.getGender()))
        print("NIP: " + str(self.getNIP()))
        print("Company Name: " + str(self.getcompanyName()))
        print("Work Status: " + self.getSleep())