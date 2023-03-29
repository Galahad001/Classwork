class Human():
    counter = 0

    def __init__(self, name):
        Human.counter = self.counter + 1
        self._name = name

    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    def getCounter(self):
        return Human.counter
    
    def out(self):
        print("Human - ", self._name)



class Builder(Human):
    counter = 0

    def __init__(self, name, prof):
        super().__init__(name)
        Builder.counter = self.counter + 1
        self.__prof = prof

    def getProf(self):
        return self.__prof
    
    def setProf(self, prof):
        self.__prof = prof

    def getCounter(self):
        return Builder.counter
    
    def out(self):
        print("Builder - ", self.__prof)



class Sailor(Human):
    counter = 0

    def __init__(self, name, prof):
        super().__init__(name)
        Sailor.counter = self.counter + 1
        self.__prof = prof


    def getProf(self):
        return self.__prof
    
    def setProf(self, prof):
        self.__prof = prof

    def getCounter(self):
        return Sailor.counter
    
    def out(self):
        print("Sailor - ", self.__prof)



class Pilor(Human):
    counter = 0
    
    def __init__(self, name, reis):
        super().__init__(name)
        Pilor.counter = self.counter + 1
        self.__reis = reis

    def getReis(self):
        return self.__reis
    
    def setReis(self, reis):
        self.__reis = reis

    def getCounter(self):
        return Pilor.counter
    
    def out(self):
        print("Pilor - ", self.__reis)

list = [Human("User"), Builder("builder", "welder"), Sailor("Jack", "Cap"), Pilor("Ivan", 100)]

def out(list):
    for i in list:
        i.out()

out(list)

print("======================")

def getCounter(list):
    for i in list:
        print(i.getCounter())

getCounter(list)