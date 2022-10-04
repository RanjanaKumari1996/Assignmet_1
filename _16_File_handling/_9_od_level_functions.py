import os


#delete a file form os

#os.remove("demo.txt")


#to check file already exist or not

# exist=os.path.exists("ranjana.txt")
# print(exist)


#remove directory rmdir
#but if a data is available in selected directory then it will not delete a dir

# os.rmdir("C:\Python\dummy")


#create file on a specific location
# file=open("C:\\Python\\_14_packages_and_modules\\ranjana.txt", "w")

# file.write("Hello ranjana singh rajput")

#x mode
#create a file but if already exists then it will generate an error
file=open("ranjana234_edoyda.txt", "x")

file.write("Hello ranjana singh rajput")


