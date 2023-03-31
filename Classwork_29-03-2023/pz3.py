class HZ():
    def __init__(self):
        pass
        # self.__kvadrat = kvadrat
        # self.__treugol1 = treugol1
        # self.__treugol2 = treugol2
        # self.__romb1 = romb1
        # self.__romb2 = romb2
    def vop(self):
        print("Какую фигуры хотите вичислить?")
        res = int(input("1 - квадрат, 2 - треугольник, 3 - ромб"))
        if res == 1:
            dan = int(input("Введите данные для высчета квадрата "))
            self.kv(dan)
        elif res == 2:
            a = int(input())
            b = int(input())
            c = int(input()) 
            self.tr(a, b, c)
        #         p = (a + b + c) / 2
        #         s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        #         print(s)

        else:
            p = int(input(6))
            q = int(input(8))
            self.rmb(p, q)
        #         res = (p*q) / 2
        #         print(res)

    def kv(self, dan):
        res = dan * dan
        print(res)

    def tr(a, b, c):
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(s)

    def rmb(p, q):
        res = (p*q) / 2
        print(res)
    

res = HZ()
res.vop()



    # def getKV(self):
    #     return self.__kvadrat
    # def setKV(self):
    #     self.__kvadrat = k

    # def kv(self, kvadrat):
    #     self.__kvadrat = self.__kvadrat * self.__kvadrat
    #     return