# from sqlite3 import ProgrammingError
# from tkinter import Variable


# local variable
# define inside the function it is called local Variable
# scope is within in the function


# global Variable
# define outside the function it is called global Variable
# scope is throughout the python file
# we can create a global variable with the help of GLOBAL keyword




subject="Computer Science"

name="Ranjana"

def add():
    no1=10 #local variable
    no2=20 #local variable
    add= no1+no2 #local variable
    print(name)
    print(subject)
    global address
    address="house number 1322"
    print(address)

add()

print(address)

#print(no1) #we can not access the local variable outside the function

print(name)
print(subject)

