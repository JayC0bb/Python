import os
clear = lambda: os.system('cls')


class vehicle:

    def __init__(self, znacka, rok, vykon):

        self.znacka = znacka
        self.rok = rok
        self.vykon = vykon

    def __str__(self):

        return f"Vozidlo bylo vyrobeno roku {self.rok} Znacka vozidla je {self.znacka} Vykon vozidla je {self.vykon}."

class truck(vehicle):

    def naklad(self, naklad="veze uhli"):

        return f"Nakladak byl vyroben roku {self.rok} Znacka nakladaku je {self.znacka} Vykon nakladaku je {self.vykon}. Nakladak {naklad}."

class motorbike(vehicle):

    def rychlost(self, rychlost="Jede"):

        return f"Motorka byla vyrobena roku {self.rok} Znacka motorky je {self.znacka} Vykon motorky je {self.vykon},{rychlost}"

class car(vehicle):
    
    def nadrz(self, nadrz="nadrze vozidla je 50L."):
        
        return f"Auto bylo vyrobeno roku {self.rok} Znacka auta je {self.znacka} Vykon auta je {self.vykon}, Objem {nadrz} "

        
clear()

print("----------", "Auto", "----------")
auto = car("Subaru Impreza.", "1993.", "152 Koní")
print(auto)
print(auto.nadrz())

print("----------", "Motorka", "----------")
motorka = motorbike("Kawasaki Vulcan Special.", "1996.", "4,5 kW")
print(motorka)
print(motorka.rychlost())

print("----------", "Nakladak", "----------")
nakladak = truck("Tatra.", "1850.", "400 Koní")
print(nakladak)
print(nakladak.naklad())
