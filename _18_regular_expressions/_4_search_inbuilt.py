import re

data="hello Ranjana"
res=re.search("Ranjana",data)
print(res)


#search is same as findall but ir returns the index of searched words
print (dir(re))