# Import/inlude objek
from lib2to3.pgen2.token import OP
from Ship import Ship
from Airplane import Airplane
from Job import Job
from Driver import Driver

# deklarasi objek
OShip = [None] * 5
OPlane = [None] * 5
Ojob = [None] * 5
ODriver = [None] * 5
for x in range(5):
    OShip[x] = Ship()
    OPlane[x] = Airplane()
    Ojob[x] = Job()
    ODriver[x] = Driver()

# mengisi objek
OShip[0].setvecship("HFO", 120, "5 Years", "Cargo", "Australia")
OShip[1].setvecship("LSFO", 30, "1.5 Years", "Cargo", "Singapore")
OShip[2].setvecship("HFO", 150, "3 Years", "Persiar", "Singapore")
OShip[3].setvecship("LSFO", 50, "2 Years", "Cargo", "Malaysia")
OShip[4].setvecship("Diesel", 100, "2.5 Years", "Tanker", "Turkey")
OPlane[0].setvecplane("AVGAS", 80, "1.5 Years", "Airbus", "40m")
OPlane[1].setvecplane("Jet Fuel", 30, "2 Years", "Regional", "35m")
OPlane[2].setvecplane("Jet Fuel", 120, "3 Years", "Airbus", "40m")
OPlane[3].setvecplane("Jet Fuel", 135, "2 Years", "Airbus", "40m")
OPlane[4].setvecplane("AVGAS", 70, "1.5 Years", "Regional", "50m")
Ojob[0].setperjob("2004222", "Shidiq", "Male", "2815", "Google", "CEO Founder")
Ojob[1].setperjob("2005222", "Arif", "Female", "1510", "Google", "President Directur")
Ojob[2].setperjob("1003661", "Ahmad", "Male", "6521", "Microsoft", "IT Consultant")
Ojob[3].setperjob("1002154", "karta", "Female", "4595", "Apple", "Product Designer")
Ojob[4].setperjob("1003541", "Nanda", "Female", "1256", "Tesla", "UI/UX Designer")
ODriver[0].setperdriver("500121", "South", "Male", "1100", "28 Oct 2050", "Car")
ODriver[1].setperdriver("896600", "North", "Female", "2200", "15 March 2051", "Car")
ODriver[2].setperdriver("321500", "Shiki", "Male", "3300", "12 Sep 2002", "Bus")
ODriver[3].setperdriver("223310", "Iris", "Female", "4400", "5 April 2002", "Bus")
ODriver[4].setperdriver("536110", "Lenka", "Female", "5500", "18 June 2025", "Motorcycle")

# menampilkan objek
print("SHIP LIST")
print("#########")
for x in range(5):
    OShip[x].Move()
    OShip[x].printship()
    print("=============\n")
print("AIRPLANE LIST")
print("#########")
for x in range(5):
    OPlane[x].Move()
    OPlane[x].printplane()
    print("=============\n")
print("JOB LIST")
print("#########")
for x in range(5):
    Ojob[x].sleep()
    Ojob[x].printjob()
    print("=============\n")
print("DRIVER LIST")
print("#########")
for x in range(5):
    ODriver[x].sleep()
    ODriver[x].printdriver()
    print("=============\n")