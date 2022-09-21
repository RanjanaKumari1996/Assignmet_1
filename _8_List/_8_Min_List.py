size = int(input("Enter the size of elements you want in your list : "))

lst = []
for i in range(size):
    element = int(input("Enter element : "))
    lst.append(element)

print("Original List:",lst)

min=0

for i in range(size):
    if min>lst[i]:
        min=lst[i]
print("minimum value in a list is:", min)