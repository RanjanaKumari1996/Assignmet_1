#set comprehension
#it is used to create a new set from another set/list/tuple
lst=[10,4,6,1,7,8,9,11,56]

result={lst[i] for i in range(len(lst)) if i in(0,2,5,7)}
print(result, type(result))