# class Animal():
#     def __init__(self):
#         print("Animal Created")
#     def whoAmI(self):
#         print("Animal")
#     def eat(self):
#         print("Eating")
# animal = Animal()
# animal.whoAmI()
# animal.eat()
# class Dog(Animal):
#     def __init__(self):
#         #Animal.__init__(self)
#         print("Dog Created")
#     def bark(self):
#         print("Woof")
#     def eat(self):
#         print("Eating Dog Food")
# dogg = Dog()
# dogg.whoAmI()
# dogg.bark()
# dogg.eat()

#special methods
class Book():
    def __init__(self, title = "XYZ", author = "ABC", pages = 0):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("a book is destroyed")
b = Book("Python", "jose", 44)
print(b)
mylist = [1, 3, 4]
print(len(b))
print(mylist)
del(b)
