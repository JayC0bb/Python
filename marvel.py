class Character:
    def __init__ (self, name = "", year = 0, date = "", weapons = [], best = ""):
        self.__Name = name
        self.__Year = year
        self.__Date = date
        self.__Weapons = weapons
        self.__Best = best
        
    def setName(self, StrName = ""):
        self.__Name = StrName

    def setYear(self, IntYear = 0):
        self.__Year = IntYear
    
    def setDate(self, StrDate = ""):
        self.__Date = StrDate

    def setBest(self, StrBest = ""):
        self.__Best = StrBest

    def getName(self):
        return self.__Name

    def getYear(self):
        return self.__Year

    def getDate(self):
        return self.__Date

    def getBest(self):
        return self.__Best

    def addWeapon(self, weapon):
        self.__Weapons = weapon

    def removeWeapon(self):
        del self.__Weapons

    def getWeapon(self):
        return self.__Weapons

character = Character()
print(character)
character.setName("Black Panther")
character.setYear(1976)
character.setDate("29.11.")
character.setBest("Chadwick Boseman")
character.addWeapon("Claws")

print("-"*25)
print("Name: ", character.getName())
print("Year: ", character.getYear())
print("Date: ", character.getDate())
print("Actor: ", character.getBest())
print("Weapons: ", character.getWeapon())
print("-"*25)