import re
data="hello ranjana"
res=re.findall(r"[lea]", data) #it checks for all l,e and a
print(res)

data="hello ranjana"
res=re.findall(r"[^ahr]", data) #it returns except a,h and r characters
print(res) 


data="hello ranjana"
res=re.findall("[a-i]", data)
print(res) #it returns characters between a to i

data="hello ranjana"
res=re.findall("[a-z]{4}", data) #it returns limited characters 
print(res)


# data="hello ranjana"
# res=re.findall(r"\Ranjana", data)
# print(res)


data="67"
res=re.findall("[4-7][6-9]", data)
print(res)

data="795"
res=re.findall("[1-9][1-9][1-9]", data)
print(res)