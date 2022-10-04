file=open('ranjana.txt', "r")

data=file.read() #read whole data
print(data)


file=open("ranjana.txt", "r")

data=file.read(5) #read from 5th character
print(data)


file=open("ranjana.txt", "r")

data=file.readline() #only read first line
print(data)

file=open("ranjana.txt", "r")

data=file.readlines() #return all lines
print(data)

for i in file: #read logically
    print(i, end="\n")
 




def f1():
    x=15
    print(x)
x=12
f1()


t=(1,2,4,3)
print(t[3])

print(max(t))
print(len(t))


x=['ab','cd']
for i in range(2):
    x[i].upper()
    print(x[i])

print("xyyzxyzxzxyy".count('yy'))

func=lambda x: return x
print(func(2))