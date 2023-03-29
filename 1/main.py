# Счетчик обьектов, !полифармизм!
class User():

    countUser = 0

    def __init__(self, firstName, age):
        User.countUser = self.countUser + 1
        self.__firstName = firstName
        self.__age = age

    def getCU(self):
        return self.countUser
    
u = User("Nick", 25)
u2 = User("Li", 19)
print(u.getCU())
print(u.getCU())

    