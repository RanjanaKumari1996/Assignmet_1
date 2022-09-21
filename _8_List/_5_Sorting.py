# Num=int(input("Please enter number of elements for a list:"))

# lst=[]
# Sort_Lst=[]

# for i in range(Num):
# 	item=int(input("Enter Element:"))
# 	lst.append(item)
# print("Original List:",lst)

# min=0
 
# i=0
# while i<Num:
# 	for j in range(1,Num+1):
# 		if lst[j]<lst[i]:
# 			min=lst[j]
# 			Sort_Lst.append(min)
# 			lst.remove(min)
# 		else:
# 			min=lst[i]
# 			Sort_Lst.append(min)
# 			lst.remove(min)

# print(Sort_Lst)
    
# i+=1

# for i in range(Num):
# 	print(Sort_Lst)

#2nd way with using nested for loop


no = int(input("Please enter the required size of list: "))

lst1 = []

for i in range(0, no ):
    element = int(input("Enter Elements :"))
    lst1.append(element)

# lst = [6,5,1,2,9]

for i in range(no):
    for j in range(i + 1, no): 
        if lst1[i] > lst1[j]:  
            # temp = lst1[i]     
            # lst1[i] = lst1[j]  
            # lst1[j] = temp     
            lst1[i],lst1[j] = lst1[j],lst1[i]
print("The list with ascending order is : ", lst1)
