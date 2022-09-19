Total_number_of_series=int(input("Please enter number of element in a series:"))

lst=[]
for i in range(Total_number_of_series-1,-1,-1):
    value=int(input("enter the value for number series:"))
    lst.append(value)


#num=[1,2,3,4,5,6,7,8,9]
#length=len(num)
Even_counter=0
Odd_counter=0
for i in range(0,Total_number_of_series):
    if (lst[i]%2==0):
        Even_counter=Even_counter+1
    else:
        Odd_counter=Odd_counter+1
print("Number of even numbers are:", Even_counter)
print("Number of odd numbers are:", Odd_counter)