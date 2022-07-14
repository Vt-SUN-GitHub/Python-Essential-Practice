class Person(object):
    def __init__(self, name, age): # self == this
        self.name = name
        self.age = age
        ...

    def eat(self):
        print(self.name + "吃饭")
        ...

    #override
    def __str__(self):
        return "name: " +self.name + "\n"+"age: "+(str)(self.age)
    ...

    def __call__(self, *args, **kwargs):
        print(self.name + args[0]+ (str)(kwargs['abc']))
        ...
    ...
p1 = Person("小姐姐", 18)
p1.eat()
print(p1.__str__())

p1("一起吃饭",abc='吗' )
