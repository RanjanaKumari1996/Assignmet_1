#Lambda is very important for interview
#Lambda Function
#it is a anonymous(unnamed, unknown) function (something which is unknown)
#it is a function without a name
#it can have any number of parameters but only single codition(expression)
#it does not have a return statement
#it helps to create one liner(line) function

#without using lambda

# def add(a,b):
#     return a+b

# result=add(10,20)
# print(result)


#with using lambda 
#it is used for only a single condition
#it is one line code
#it can take n number of parameters


# syntax--> lambda <arg1,arg2>: <condition or expression>


result=lambda a,b: a+b
print(result(10,20))
