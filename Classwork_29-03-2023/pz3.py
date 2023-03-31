class Figur():
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2


    def getP1(self):
        return self.parameter1
    
    def getP2(self):
        return self.parameter2
    
    def setOut(self, parameter1, parameter2):
        print("Какую фигуры хотите вычислить?")
        vop = int(input("1 - квадрат, 2 - треугольник, 3 - ромб: "))
        if vop == 1:
            S =  self.parameter1 * self.parameter2
            return S
        elif vop == 2:
            S =  (1/2) * self.parameter1 * self.parameter2
            return S
        else:
            S = (1/2) * self.parameter1 * self.parameter2
            return S

res = Figur(2, 2)
print(res.setOut)

#         pass
#         # self.__kvadrat = kvadrat
#         # self.__treugol1 = treugol1
#         # self.__treugol2 = treugol2
#         # self.__romb1 = romb1
#         # self.__romb2 = romb2
#     def vop(self):
#         print("Какую фигуры хотите вичислить?")
#         res = int(input("1 - квадрат, 2 - треугольник, 3 - ромб"))
#         if res == 1:
#             dan = int(input("Введите данные для высчета квадрата "))
#             self.kv(dan)
#         elif res == 2:
#             a = int(input())
#             b = int(input())
#             c = int(input()) 
#             self.tr(a, b, c)
#         #         p = (a + b + c) / 2
#         #         s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#         #         print(s)

#         else:
#             p = int(input(6))
#             q = int(input(8))
#             self.rmb(p, q)
#         #         res = (p*q) / 2
#         #         print(res)

#     def kv(self, dan):
#         res = dan * dan
#         print(res)

#     def tr(a, b, c):
#         p = (a + b + c) / 2
#         s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#         print(s)

#     def rmb(p, q):
#         res = (p*q) / 2
#         print(res)
    

# res = HZ()
# res.vop()



#     # def getKV(self):
#     #     return self.__kvadrat
#     # def setKV(self):
#     #     self.__kvadrat = k

#     # def kv(self, kvadrat):
#     #     self.__kvadrat = self.__kvadrat * self.__kvadrat
#     #     return