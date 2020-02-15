# my_list = [1, 2, 3]
# my_list.append(12)
# print(my_list)
# print(type(my_list))
# class MyClass():
#     pass
# x = MyClass()
# print(type(x))
#
# myList = [1, 2, 3]
# print(type(dict))
# print(22+11)


# Video 2
# class Dog():
#     pass
# class Dog():
#     # Class object Attribute
#     kingdom = "animalia"
#
#     def __init__(self, breedvar, breedAge = "12"):
#         self.breed = breedvar
#         print("init has been accessed")
#         self.age = breedAge
#         # pass
#
# Rusty = Dog("Lab", 22)
# print(type(Rusty))
# print(Rusty.breed)
# print(Rusty.age)
# Rusty.breed = "Boxer"
# print(Rusty.breed)
# print(Rusty.age)
# Rusty.__init__("Lab")
# print(Rusty.breed)
# print(Rusty.age)
# print(Rusty.kingdom)

class Circle():
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
    def area(self):
        return (self.radius**2)*Circle.pi
    def changeRadius(self, radius = 0):
        self.radius = radius

myC = Circle(22)
print(myC.radius)
print(myC.area)
print(myC.area())

myC.radius = 100
print(myC.area())
myC.changeRadius()
print(myC.area())
myC.changeRadius(6783)
print(myC.area())
