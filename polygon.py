class Polygon:
    def __init__(self):
        pass
    def set(self):
        pass
    def numofsides(self):
        return self.__num

class Triangle(Polygon):
    def __init__(self, **kwargs):
        self.__num = int(kwargs["keys"]) if "keys" in kwargs.keys() else 0
    def set(self, st=""):
        self.__num=st
    def numofsides(self):
        return self.__num

class Pentagon(Polygon):
    def __init__(self, **kwargs):
        self.__num = int(kwargs["keys"]) if "keys" in kwargs.keys() else 0
    def set(self, st=""):
        self.__num=st
    def numofsides(self):
        return self.__num

class Octagon(Polygon):
    def __init__(self, **kwargs):
        self.__num = int(kwargs["keys"]) if "keys" in kwargs.keys() else 0
    def set(self, st=""):
        self.__num=st
    def numofsides(self):
        return self.__num

triangle=Triangle()
pentagon=Pentagon()
octagon=Octagon()
triangle.set(3)
pentagon.set(5)
octagon.set(8)

print("The triangle's number of sides is:", triangle.numofsides())
print("The pentagon's number of sides is:", pentagon.numofsides())
print("The octagon's number of sides is:", octagon.numofsides())