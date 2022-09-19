num=int(input("enter a number for a fibonacci series:"))
no1=0
no2=1
sum=0
if num<=0:
    print("Please enter the number greater than Zero(0)")

for i in range(0,num):
    print(sum, " ")
    no1=no2
    no2=sum
    sum=no1+no2

