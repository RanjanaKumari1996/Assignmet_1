import re
data="hello ranjana"
res=re.findall(r"\Ahello", data)
print(res)

data="hello ranjana"
res=re.findall(r"\BRanjana", data)
print(res)

data="hello ranjana"
res=re.findall(r"\d", data) #return digits
print(res)


data="hello ranjana"
res=re.findall(r"\D", data) #return characters
print(res)


data="hello ranjana"
res=re.findall(r"\s", data) #return number of spaces
print(res)

data="hello ranjana"
res=re.findall(r"\S", data) #it return characters without any space
print(res)


data="hello ranjana 123659874566"
res=re.findall(r"566\Z", data) #check the end of stirng
print(res)


data="hello ranjana $%^%#WQ$@#%#^ #%^#^%#@@% ____________________"
res=re.findall(r"\w", data) #it return the characters from A-Z a-z and 0-9 spaces
print(res)



data="hello ranjana @@@@@@@ 409850 358909 #$%@%^%@^$%^##% ________"
res=re.findall(r"\W", data) #it return only the spaces, opposite of w
print(res)



