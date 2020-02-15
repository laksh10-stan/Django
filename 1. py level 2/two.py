import one
print("top level two.py")
one.func()
if __name__ == '__main__':
    print("two.py direct")
else:
    print("two.py is being imported")
