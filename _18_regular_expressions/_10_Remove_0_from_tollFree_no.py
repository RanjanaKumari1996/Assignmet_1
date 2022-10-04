import re

data="1800 0002 2020"
res=re.sub('0','',data)
print(res)