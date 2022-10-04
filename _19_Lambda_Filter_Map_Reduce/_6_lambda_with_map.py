#Without using map


lst=[4,5,61,10,15,20,2,8,63,96,85,74,48,96,12]

# def square(data):
#     sq_lst=[]
#     for i in lst:
#         sq=i**2
#         sq_lst.append(sq)
#     return sq_lst

# squarelst=square(lst)
# print(squarelst)


#With using the Map
#it is using with function 
#it is performed on the whole list but filter is working with the necessary data of a list


# def square(data):
#     return data**2

# sq_lst=list(map(square,lst))
# print(sq_lst)

#Lambda with map

square=list(map(lambda lst: lst**2,lst))
print(square)