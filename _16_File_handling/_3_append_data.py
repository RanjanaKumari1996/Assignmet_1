
#a

file=open("data_append.txt","a") #file_name\file_path, mode
file.write("Have a good day dear" " ")
file.write("Ranjana" " ")
file.write("Singh" " ")
file.write("Rajput" " ")



#a+

file=open("data_append2.txt","a+")
file.write("Pythion is a programming language")
data=file.read()
print(data)