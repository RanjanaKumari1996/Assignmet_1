import re

emailid=input("Please enter your pancard number:")

res=re.compile("^[a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$")
result=res.search(emailid)

print(result)

if res:
    print("Correct")
else:
    print("Incorrect")
#compile() method
# it is used to compile a regular expression pattern 
# provided as a string into a regex pattern object ( re. Pattern ).
# Later we can use this pattern object to search for a match inside different target strings using regex methods such as a re. match() or re.search()