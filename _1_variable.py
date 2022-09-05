from email.headerregistry import SingleAddressHeader
from operator import truediv
from pickle import TRUE, TUPLE1
from unicodedata import decimal, digit


# num= "my life is my rule"
# print(num)
# #dedicated
# print(type(num))
# float_var= 25.3561544656
# float_var_type= type(float_var)
# print(float_var_type)
# night_var= True
# print(type(night_var))
# comp_var= 2+69j
# print(type(comp_var))
# none_var=  None
# print(type(none_var))

#list
#list allows you to store heterogenous data
#duplicate values are allowed
#mutable (modifiable)
#lsit()
#ordered= it considered the same order of data that you have entered in the list
#iterable= that is countable in nature
# lst=[10,20,30,40,50,60,70,80,90,100, "ranajan", True,20,10,30,40] 
# print(lst)
# print(lst[6])
# # print(lst[12])
# # #print(lst[10])
# # lst[10]= "Ravi Singh"
# # print(lst[10])

# # lst1= list([250,89,45,78,96])
# # print(lst1)
# # print("lst type is=", type(lst))
# # print("lst1 type is=", type(lst1))

# #tuple
# #are used to store more than one value
# #()
# #tuple()
# #ordered
# #indexed
# #immutable (can not change)
# #contans duplicate values


# tup = (10,78,20,59,89,48)
# print(tup)
# tup1= tuple((52,85,96,78,96,"ranvi", True))
# print(tup1)
# print(tup1[5])
# #tup1[5]= "ravi"
# print(tup1[5])
# print("type of tup is=", type(tup))
# print("type of tup1 is=", type(tup1))

#set
#{}
#set()
#unordered
#mutable(modifiable)
#can not contain duplicate values
#non indexed

# set1= {10,58,78,96,45,12,58}
# print(set1)
# set2= set({50,50,50,50,50,50,"ranjana", True})
# print(set2)
# print("set2 type is=", type(set2))
# print("set1 type is=", type(set1))


dict= {1:"ranjana", 2: 265, 6: True, 9: 'my world', 1:"ranvi"}
print(dict)

dict[2]="Ravi"
print(dict[2])
print("Types of dict is=", type(dict))