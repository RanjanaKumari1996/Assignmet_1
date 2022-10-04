#Slicing is a operator
#syntax : [start_range : end_range : step]
#it is used to get the substring from the string

str1="Pyhton is Programming Language"

print("Original String Is : ",str1)

substring=str1[-1::-1] #working as reverse of string
print(substring)


# substring=str1[0:11:1]
# print(substring)


substring=str1[22:30:1]
print(substring)


substring=str1[:6] #by default it considers starting range as 0
print(substring)


substring=str1[12:] #by deafault it consider end  of string
print(substring)


substring=str1[:] #it will consider the whole string
print(substring)


substring=str1[-1:] #start reading the string from the end
print(substring)


substring=str1[-8:-4]
print(substring)


substring=str1[::-1] #reverse of string
print(substring)

str2="Ranjana"

reverse=str2[::-1]
print(reverse)