size = int(input("Enter the size of elements you want in your list : "))

lst = []
for i in range(size):
    element = int(input("Enter element : "))
    lst.append(element)

print("Original List:",lst," ")
rev_lst=[]

for i in range(size-1,-1,-1):
    
    rev_lst.append(lst[i])
    
print("Reverse List:",rev_lst)
