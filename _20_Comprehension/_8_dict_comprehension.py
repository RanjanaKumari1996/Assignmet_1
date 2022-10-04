#dictionary comprehension
#it is used to create a new dictionary from another datatype
# str1="python"

# #o/p={"P":"p","Y":"y"}

# dict_compre={i.upper() : i.lower() for i in str1}
# print(dict_compre, type(dict_compre))


#dictionary with zip function

# keys=[1,2,3,4,5,6,7,8,9,10,11]
# values=[10,20,30,40,50,60,70,80,90,100,110]
# dict1={k:v for k,v in zip(keys,values)}
# print(dict1)



#dictionary without zip function

# keys=[1,2,3,4,5,6,7,8,9,10,11]
# values=[10,20,30,40,50,60,70,80,90,100,110]
# dict1={keys[i]:values[i] for i in range (len(keys))}
# print(dict1)


# [4,5,8,1,2,3]
#[4:[table of 4], 5:[table of 5]]

# lst=[4,5,8,1,2,3]
# dict1={j: [i*j for i in range(1,11)] for j in lst}
# print(dict1)

#Create a new with same values that are in lst1 and lst2

lst1=[1,2,3,4,5]
lst2=[4,5,6,7,8]
result=[i for i in lst1 for j in lst2 if i==j]
print(result)