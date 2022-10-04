#r read

# file=open("demo.txt", "r")
# data= file.read()
# print(data)  



# file=open("demo.txt") #by default read mode

# data= file.read()
# print(data)  


#r+ 

file=open("demo.txt", "r+")
data= file.read()
print(data)  
file.write("Good night")