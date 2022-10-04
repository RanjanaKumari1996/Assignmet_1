# Without using filter

lst=[4,5,61,10,15,20,2,8,63,96,85,74,48,96,12]
# def even(lst):
#     even_lst=[]
#     for i in lst:
#         if i%2==0:
#             even_lst.append(i)
#     return even_lst

# evlst=even(lst)
# print(evlst)


# With filter
# It is used with only function
# filter is working as just giving the necessary data 

# def even(lst):
#     return lst%2==0

# evenlst=list(filter(even,lst))
# print(evenlst)


#Lambda with filter

even_lst=list(filter(lambda lst:lst%2==0,lst))
print(even_lst)