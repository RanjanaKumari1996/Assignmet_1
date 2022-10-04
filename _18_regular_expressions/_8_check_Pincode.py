from ast import Break
import re
pincode=input("Please enter your pincode:")
#pincode_int=int(pincode)

# if pincode_int ==0:
#     print("Enter a digit greater than 0")

# else:
#     length=len(pincode)

#     #res=re.findall("\d{6}",pincode)
#     if length ==0:
#         print("Enter correct pincode")
#     elif length>6:
#         print("Enter 6 digits pincode")
#     else:
#         res=re.findall("\d{6}",pincode)
#         print(res)

res=re.findall("^[1-9]{1}[0-9]{5}$",pincode)
if res:
    print("It is correct")
else:
    print("it is incorrect")