import re

mobileno="87-28 08-06 97"
res=re.sub("\D","",mobileno)
print(res)

mobileno="87-28 08-06 97"
res=re.sub("\D","   ",mobileno)
print(res)

mobileno="87-28 08-06 97"
res=re.sub("\D","?????",mobileno)
print(res)
