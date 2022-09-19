no=int(input("Enter a number:"))
if no!=1:
    for i in range(2,no):
        if no%i==0:
            print("Composite number")
            break
    
    else:
        print("Prime number")
else:
    print("neither a prime nor a composite number")
