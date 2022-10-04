lst=["Bharati","Ranjana","Lata","sangita","Mani"]
lst_A=[]

length=len(lst)
str1=[]

for i in range(length):
    str1=str(lst[i])
    str1.append(lst[i])
    print(str1[i])
    length2=len(str1)
    for j in range(length2):
        if(str1[j]=="a" or str1[j]=="A"):
            lst_A.append(str1[j])
    print(lst_A)            
