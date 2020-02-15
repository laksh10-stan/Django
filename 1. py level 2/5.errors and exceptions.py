# try:
#     print(kk)
# except NameError:
#     print("OOOOOO ohhh")


# try:
#     f = open("simple.txt", "w")
#     f.write("dsofnowef")
# except IOError:
#     print("Couldn't find")
# else:
#     print("SUCCESS")
#     f.close()


# try:
#     f = open("simple.txt", "r")
#     f.write("dsofnowef")
# except IOError:
#     print("Couldn't find")
# else:
#     print("SUCCESS")
#     f.close()

try:
    f = open("simple.txt", "w")
    f.write("dsofnowef")
except:
    print("Couldn't find")
else:
    print("SUCCESS")
    f.close()
finally:
    print("This has to be done")
