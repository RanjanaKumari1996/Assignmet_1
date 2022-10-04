#list comprehension---> it is used for creating new list from another list

#basic format of using loop

# for i in list:
#     if<condition>:
#         <body>


#list comprehension format----->
#[body for i in lst if <condition>]


data=[5,6,3,4,8,7,5,96,4,1,5,8,4,8,6,5]

#Without list comprehension

# new_lst=[]
# for i in data:
#     new_lst.append(i)
# print(new_lst)

#with list comprehension
#for loop is compulsary

new=[i for i in data]
print(new)