class Animal(object):
    __type = '动物'

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        ...

    def getName(self):
        return self.name

    def getAge(self):
        return self.__age

    def setAge(self, value):
        self.__age = value
        ...

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
        ...

    # @age.getter
    # def age(self):
    #     return self.__age

    ...

cat = Animal('猫',18)
print(cat.getName())
print(cat.age)
cat.age = 5
print(cat.getAge())
cat.setAge(10)
print(cat.age)



