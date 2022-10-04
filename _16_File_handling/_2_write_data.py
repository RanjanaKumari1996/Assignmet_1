#W write mode

# file=open("demo.txt","w") #file_name\file_path, mode
# file.write("Have a good day dear")


#w+
file=open("demo.txt","w+") #file_name\file_path, mode
file.write("Have a good day dear")
file.seek(0,0)
data= file.read()
print(data)  

