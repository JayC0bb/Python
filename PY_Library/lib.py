class LeapYear():
    def __init__(self):
        pass

    def checkLeapYear(self):
        year = input("year:")
        if (year % 400 == 0) and (year % 100 == 0):
            #Pokud je rok dělitelný 4, je přestupný
            print("{0} is a leap year".format(year))
        elif (year % 4 ==0) and (year % 100 != 0):
            print("{0} is a leap year".format(year))
            #Pokud rok není dělitelný 4, není přestupný
        else:
            print("{0} is not a leap year".format(year))