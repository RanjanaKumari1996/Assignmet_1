import re

emailid=input("Please enter your Email Id:")

res=re.findall("^[a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$", emailid)
if res:
    print("Correct")
else:
    print("Incorrect")