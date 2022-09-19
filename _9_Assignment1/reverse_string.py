from asyncio.windows_events import NULL


str1=input("Enter a msg to mirror dimension of entered msg:")
length=len(str1)

if length==0:
    print("Please enter a word")
elif length==1:
    print("Please enter the character more than 1 so that it can be reversed")
else:
    for i in range(length-1,-1,-1):
        print(str1[i])