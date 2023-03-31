class Drob():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f"{self.__x} {self.__y}"

    def __add__(self, other):
        y = self.__y * other.__y
        ch1 = other.__y * self.__x
        ch2 = other.__x * self.__y
        x = ch1 + ch2
        return Drob(x, y)
    
    def __sub__(self, other):
        y = self.__y * other.__y
        ch1 = other.__y * self.__x
        ch2 = other.__x * self.__y
        x = ch1 - ch2
        return Drob(x, y)
    


a = Drob(5, 7)
b = Drob(4, 20)
c = a.__add__(b)
d = a.__sub__(b)
print(d.__str__())
print(c.__str__())


# a = Fraction(5, 7)
# b = Fraction(4, 20)

# print(math.gcd(7, 20))







# class Num():

#     def __init__(self, num):
#         self.__num = num

#     def __add__(self, other):
#         n = self.__num + other.__num
#         return Num(n)

#     def __sub__(self, other):
#         n = self.__num - other.__num
#         return Num(n)
    
#     def __mul__(self, other):
#         n = self.__num * other.__num
#         return Num(n)
    
#     def __truediv__(self, other):
#         if other.__num != 0:
#             n = self.__num / other.__num
#             return Num(n)
#         else:
#             print("num is 0")
    
#     def __str__(self) -> str:
#         return f" number = {self.__num}"
    
# a = Num(2)
# b = Num(4)

# addNum = a.__add__(b)
# subNun = a.__sub__(b)
# mulNum = a.__mul__(b)
# truedivNum = a.__truediv__(b)

# print(addNum)
# print(subNun)
# print(mulNum)
# print(truedivNum)

