class Vector():

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f" {self.__x} {self.__y}"
    
    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y
        return Vector(x, y)

    

v = Vector(10, 20)
v2 = Vector(15, 25)
v3 = v.__add__(v2)
print(v3.__str__())

# print(v + v2)
# print(v.__str__())
