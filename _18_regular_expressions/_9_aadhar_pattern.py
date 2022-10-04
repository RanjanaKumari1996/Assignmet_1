import re
adhar=input("Please enter your Aadhar card number:")
res=re.findall("^[1-9]{1}[0-9]{3}[-][0-9]{4}[-][0-9]{4}$",adhar)


if res:
    print("It is correct",)
else:
    print("It is incorrect")
