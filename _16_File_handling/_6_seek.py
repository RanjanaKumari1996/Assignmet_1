#seek 
#it allows you to modify the cursor position

#seek(offset, from what)
#offset= number of positions to move forward
#from what= point of reference

#from what parameters---->
#0- beginning
#1- current position
#2- end of file
#by default value if 0
#for text fiels only 0 works 1 and 2 doesn't works

file=open("data_append.txt", "w") 


pos=file.tell()

print("before seek:",pos)

file.write("My duty is always on the high priority")


file.seek(6,0)
file.write("Hello Everyone")
pos=file.tell()
print("after seek:",pos)