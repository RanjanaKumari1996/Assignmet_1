from functools import reduce

#reduce combine the elements of a list and combine the elements of a list
#reduce is used when you want to sum, product of list elements
#it is used when you need only a single output

#Without using reduce

lst=[4,5,61,10,15,20,2,8,63,96,85,74,48,96,12]


# def sum(data):
#     sums=0
#     for i in lst:
#         sums+=i
#     return sums

# result=sum(lst)
# print(result) 


#With using Reduce
#it is working with function

# def sum(data1,data2):
#     return data1+data2

# result=reduce(sum,lst)

# print(result)

#Lambda with Reduce

result=reduce(lambda data1,data2:data1+data2,lst)
print(result)