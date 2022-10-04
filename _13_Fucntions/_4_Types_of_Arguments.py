
# types of arguments/parameters
# 1. required/positinal argument
# 2. default argument
# 3. keyword argument
# 4. variable_length argument
#   a) arbitary positional argument (known as *args)
#   b) arbitary keyword positional argument (known as **kwargs)


#1. required/positional argument

# def student(rno, name):
#     print("Roll number:", rno, "Name:", name)


# #student(22,"Ranjana Bhushan")
# student("Roshan bhushan", 15) 


#2. default argument

# def student(rno=20, name="Ranju Singh Rajput"): #def student(rno, name="Ranju Singh Rajput"):, 
#                                                 #if you have started to make a function with default parameter
#                                                 # # then every variable should have to mention a default variable 
#     print("Roll number:", rno, "Name:", name)
#     print(end="\n")


# student()
# student(36, "Mohan payare")
# student(69)
# student("","56")


#3. keyword argument

# def numbers(no1, no2=30, no3=90, no4=100):
#     print(no1, " " , no2, " ",no3, " ", no4 )
 
# numbers(10)
# numbers(500,968) # i want to update the value of no3 but its not working now i use keyword argument 
# numbers(no1=58,no4=85)
# numbers(no1=596, no3=1000)


#4. variable length argument
    # a) *args

# def users(*args):
#     print(args, type(args))
#     for i in args:
#         print(i)
#     print(args[21])


# users(10,52,6,9,58,14,52,8,5,48,5,8,6,2,8,6,3,526,5,8,[10,20,30,50,60,48], "Ranjana")

    # b) **kwargs

def users(**kwargs):
    print(kwargs, type(kwargs))
    for k, v in kwargs.items():
        print(k, "----->>", v)
    

    
users(one="Bharati", two="Rnajana", three="Roshan")
