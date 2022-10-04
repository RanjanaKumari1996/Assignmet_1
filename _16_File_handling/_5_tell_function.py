#tell function is used to tell the postion of cursor in a file


#by default read mode, it always give the cursor positiion 0
file=open("data_append.txt")



pos=file.tell()

print(pos)


#write mode, it always give the cursor positiion 0 beczz it initial writing the data
file=open("data_append.txt", "w") 


pos=file.tell()

print("before writing:",pos)

file.write("My duty is always on the high priority")
pos=file.tell()

print("after writing:",pos)
