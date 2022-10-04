# str1="Pyhton is a programming language"


# print(str1[1])
# length=len(str1)
# count=0
# long=0

# for i in range(length):
#     if str1[i]!=" ":
#         count+=1
#         print(count)
        
#     # long=count
#     # if 





#     l1=[1,3,5,7,9]
#     l2=[2,4,6,8,10]

#     index=0
#     for i in range(1,11,2):
#         l1.insert(i,l2[index])
#         index+=1
#         print(l1)


#     a,b,c=(1,2,3,4,5,6,7,8,9) [1::3]
#     print(b)
#     print(a)
#     print(c)


#     t=('foo',)
#     print(t, type(t))



#     lst=[1,2,3,4,5]
#     lst.remove(3)
#     print(lst)

#     lst=[1,2,3,4,5]
#     del lst[2]
#     print(lst)


#     l1=[[1,2,3], [4,5,6]]
#     l2=[]
#     for list1 in l1:
#         l2.extend(list1)
#     print(l2)


#     a=['foo','bar','baz', 'qux','quux', 'corge']
#     print(a[4::-2])


#     print(['a','b','c']==['c','a','b'])



alphadict={}
for i in range(ord('a'),ord('b')+1):
    #alphadict[chr(i)=i]
    print(alphadict)


d={'foo':100, 'bar':200, 'baz':300}
#print(d['bar':'baz'])
d={}
d['foo']=100
d['bar']=200
d['baz']=300
print(d)


country_counter={}
def addone(country):
    if country in country_counter:
        country_counter[country]+=1
    else:
        country_counter[country]=1


addone("India")
addone("Japan")
addone("USA")

print(len(country_counter))


def outfun(a,b):
    def innerfun(c,d):
        return c+d
    return innerfun(a,b)
    return a

result=outfun(5,10)
print(result)


def fun(num):
    return num+25
fun(5)
#print(num)


def display(**kwargs):
    for i in kwargs:
        print(i)
display(name="mma", age="25")



goa={'tshirts':"Dukesssss sfkjakllks fsijklj idfj", 'shorts':'nike,Abbibas,pama'}
def ingoa(tshirts,shorts):
    print("i love to wear", tshirts.split(' ')[0])

ingoa(**goa)

# random

# #r=random.randrange(10,20,2)

# r=random.randrange(10,20)

# r=random.randint(10,20)

#r=random.randint(10,21)

x=[10,52,85,96,545,2,45,4]
y=x.sort()
print(y)


x='happy'
def myfun(a):
    print(x)
    x='sad'

myfun('mango')
print(x)