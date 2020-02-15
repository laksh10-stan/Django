# x = 25
# def my_func():
#     x = 200
#     return x
# print(x)
# print(my_func())
# print(x)
# print(len)
# print(SyntaxError)
# lambda x: x**2
# print(lambda x(12))
x = 12
name = "Global"
def greet():
    # name = "sammy"
    global x
    x = 34
    def hello():
        print(name)
    hello()
greet()
print(x)
