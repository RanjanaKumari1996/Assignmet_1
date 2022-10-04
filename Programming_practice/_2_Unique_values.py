lst=[5,6,3,1,3,5,2,4]

length=len(lst)

print(length)

for i in range(length):
    if lst[i]==lst[i+1]:
        lst.remove(lst[i])
    
    
print(lst)       
