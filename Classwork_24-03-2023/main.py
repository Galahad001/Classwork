class Transport():
    def __init__(self, speed, oil):
        self._speed = speed
        self._oil = oil

    def setSpeed(self):
        self._speed = input("Enter speed: ")

    def setOil(self):
        self._oil = input("Enter oil: ")

    def getSpeed(self):
        return self._speed
    
    def getOil(self):
        return self._oil

    speed = property(getSpeed, setSpeed)
    oil = property(getOil, setOil)

    def out(self):
        print(self.speed, self.oil)


# class Auto(Transport):
#     def __init__(self, speed, oil, color):
#         super().__init__(speed, oil)
#         self.__color = color

#     def getColor(self):
#         return self.__color
    
#     def setColor(self, color):
#         self.__color = color

#     color = property(getColor, setColor)

#     def out(self):
#         print(self.speed, self.oil, self.color)

# m = Auto(150, "95", "red")
# print(m.getSpeed(), m.getOil(), m.getColor())

# m.auto = "green"
# print(m.getSpeed(), m.getOil(), m.getColor())

# listTr = [Transport(50, "92"), Auto(100, "95", "red"), Transport(120, "95"), Auto(200, "92", "green")]

# def out(transport):
#     for t in transport:
#         t.out()

# out(listTr)


class Land(Transport):
    def __init__(self, speed, oil, model):
        super().__init__(speed, oil)
        self._model = model

    def setModel(self):
        self._model = input("Enter model")

    def getModel(self):
        return self._model

    model = property(getModel, setModel)


    def out(self):
        print(self.speed, self.oil, self.model)


class Auto(Land):
    def __init__(self, speed, oil, model, color):
        super().__init__(speed, oil, model)
        self.__color = color

    def setColor(self):
        self.__color = input("Enter color")

    def getColor(self):
        return self.__color
    
    color = property(getColor, setColor)

    def out(self):
        print(self.speed, self.oil, self._model, self.color)


class Air(Transport):
    def __init__(self, speed, oil, marka):
        super().__init__(speed, oil)
        self._marka = marka

    def setMarka(self):
        self._marka = input ("Enter marka")

    def getMarka(self):
        return self._marka
    

    marka = property(getMarka, setMarka)

    def out(self):
        print(self.speed, self.oil, self.marka)


class Airplane(Air):
    def __init__(self, speed, oil, marka, pas):
        super().__init__(speed, oil, marka)
        self.__pas = pas

    def setPas(self):
        self.__pas = input("Enter pas")  

    def getPas(self):
        return self.__pas
    

    pas = property(getPas, setPas)

    def out(self):
        print(self.speed, self.oil, self.marka, self.pas)


class Wtr(Transport):
    def __init__(self, speed, oil, tanege):
        super().__init__(speed, oil)
        self._tanege = tanege

        
    def setTannege(self):
        self._tanege = input("Enter tanege")

    def getTanege(self):
        return self._tanege

    tanege = property(getTanege, setTannege)

    def out(self):
        print(self.speed, self.oil, self.tanege)


class Ship(Wtr):
    def __init__(self, speed, oil, tanege, type):
        super().__init__(speed, oil, tanege)
        self.__type = type

    def setType(self):
        self.__type = input("Enter type")
   
    def getType(self):
        return self.__type
    

    type = property(getType, setType)

    def out(self):
        print(self.speed, self.oil, self.tanege, self.type)


listT = [Transport(90, "92"), Land(100, "95", "BMV"), Auto(190, "92", "BMV", "red"), Air(300, "92", "boing"), Airplane(400, "95", "airo", "300"), Wtr(54, "solara", "500"), Ship(360, "92", "800", "Gruzovoi")]
list_0 = listT[0]
list_1 = listT[1]
list_2 = listT[2]
list_3 = listT[3]
list_4 = listT[4]
list_5 = listT[5]
list_6 = listT[6]


list_0.setSpeed()
list_0.setOil()
list_1.setModel()
list_2.setColor()
list_3.setMarka()
list_4.setPas()
list_5.setTannege()
list_6.setType()

def out(transport):
    for t in transport:
        t.out()

out(listT)
