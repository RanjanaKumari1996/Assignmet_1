import re

pancard=input("Please enter your pancard number:")

res=re.findall("^[A-Z]{5}[0-9]{4}[A-Z]{1}$",pancard)

if res:
    print("Correct")
else:
    print("Incorrect")
