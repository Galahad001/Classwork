class Passport():
    counter = 0

    def __init__(self, FIO, age, city, registr, yin, semPol):
        Passport.counter = self.counter + 1
        self._FIO = FIO
        self._age = age
        self._city = city
        self._registr = registr
        self._yin = yin
        self._semPol = semPol

    
    def getFIO(self):
        return self._FIO

    def getAge(self):
        return self._age
    
    def getCity(self):
        return self._city
    
    def getRegistr(self):
        return self._registr
    
    def getYin(self):
        return self._yin
    
    def getSemPol(self):
        return self._semPol
    
    def setFIO(self, FIO):
        self._FIO = FIO

    def setAge(self, age):
        self._age = age
    
    def setCity(self, city):
        self._city = city
    
    def setRegistr(self, registr):
        self._registr = registr
    
    def setYin(self, yin):
        self._yin = yin
    
    def setSemPol(self, semPol):
        self._semPol = semPol

    def getCounter(self):
        return Passport.counter
    
    FIO = property(getFIO, setFIO)
    age = property(getAge, setAge)
    city = property(getCity, setCity)
    registr = property(getRegistr, setRegistr)
    yin = property(getYin, setYin)
    semPol = property(getSemPol, setSemPol)

    def out(self):
        print("FIO - ",self.FIO,"\n","Age - ",self.age,"\n","City - ",self.city,"\n","Registr - ",self.registr,"\n","Yin - ",self.yin,"\n","SemPol - ",self.semPol)
        # print("FIO - ", self._FIO)
        # print("Age - ", self._age)
        # print("City - ", self._city)
        # print("Registr - ", self._registr)
        # print("Yin - ", self._yin)
        # print("SemPol - ", self._semPol)



class ForeiginPassport(Passport):
    counter = 0

    def __init__(self, FIO, age, city, registr, yin, semPol, visa, namberZP):
        super().__init__(FIO, age, city, registr, yin, semPol)
        ForeiginPassport.counter = self.counter + 1

        self.__visa = visa
        self.__namberZP = namberZP

    def getVisa(self):
            return self.__visa
        
    def getnamberZP(self):
            return self.__namberZP
        
    def setVisa(self, visa):
        self.__visa = visa

    def setNamberZP(self, namberZP):
        self.__namberZP = namberZP

    def getCounter(self):
        return ForeiginPassport.counter
    
    visa = property(getVisa, setVisa)
    namberZP = property(getnamberZP, setNamberZP)
    
    def out(self):
        print("\nVisa - ", self.visa, "\n", "NamberZP - ", self.namberZP)
        # print("Visa - ", self.__visa)
        # print("namberZP - ", self.__namberZP)


list = [Passport("Алексеев Алексей Александрович", 25, "Сочи", "Центр", '1234546', "Холост"), ForeiginPassport("Иванович Петр Филипов", 23, "Казахстан", "Центр", '15346553', "Женат", 'Номер Визы XXXXXXXXX', "7560487503495")]

def out(passport):
    for i in passport:
        i.out()

out(list)

def getCounter(list):
    for i in list:
        print(i.getCounter())

getCounter(list)








    


