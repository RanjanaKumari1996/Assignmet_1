import re

data="Hello RanjaNA"
res=re.findall("[A-Z]", data) #pattern, data 
#this pattern will give weather your data contain A-Z pattern
print(res)

data="Hello RanjaNA"
res=re.findall("[A-z]", data) #pattern, data 
#this pattern give consider all pattern
print(res)


data="Hello RanjaNA"
res=re.findall("[A-Z a-z]", data) #pattern, data 
#this pattern will give weather your data contain A-Z pattern
print(res)



data="Hello RanjaNA"
res=re.findall("[h-k]", data) #pattern, data 
#this pattern will give weather your data contains from h-k pattern
print(res)


data="Hello RanjaNA 1236"
res=re.findall("\d", data) #pattern, data 
#this will check the digits
print(res)


data="python Is A programming Language"
res=re.findall("is|a|languagesd|Is|A|Language", data) #pattern, data 
#this will check for a particular pattern
print(res)



data="Hello RanjaNA"
res=re.findall("Ran....", data) #pattern, data 
#this will check for missing characters
print(res)


data="Hello RanjaNA"
res=re.findall("R.....A", data) #pattern, data 
#this will check for a missing characters
print(res)



data="Hello RanjaNA"
res=re.findall("R.*A", data) #pattern, data 
#this will check for multicharacters missing pattern
print(res)


data="Hello RanjaNA"
res=re.findall("H*", data) #pattern, data 
#this will check for character position in the list
print(res)

data="Hello RanjaNA"
res=re.findall("R.*", data) #pattern, data 
#for multicharacters
print(res)

data="Hello RanjaNA"
res=re.findall("R.?j", data) #pattern, data 
#for single character
print(res)

data="Hello RanjaNA"
res=re.findall("R.?", data) #pattern, data 
#single character
print(res)


data="Hello RanjaNA"
res=re.findall("R.{3}A", data) #pattern, data 
#for specific number of characters
print(res)


data="Hello RanjaNA"
res=re.findall("R.{5}A", data) #pattern, data 
#for specific charcters
print(res)


data="Hello RanjaNA"
res=re.findall("^H.*A", data) #pattern, data 
#with cap stands for beginning
print(res)

data="Hello RanjaNA"
res=re.findall("A$", data) #pattern, data 
#with dollar stands for end of string
print(res)