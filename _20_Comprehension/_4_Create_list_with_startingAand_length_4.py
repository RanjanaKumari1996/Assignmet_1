lst=["Apple","ac","mango","Aeroplane","laptop","Apply","diary","mobile","agreement","account"]

result=[i for i in lst if len(i)>=4 and (i.startswith("A") or i.startswith("a"))]

print(result)