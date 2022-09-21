size = int(input("Enter the size of elements you want in your list : "))

lst = []
for i in range(size):
    element = int(input("Enter element : "))
    lst.append(element)

print("Original List:",lst)

max=0

for i in range(size):
    if max<lst[i]:
        max=lst[i]
print("maximum value in a list is:", max)
