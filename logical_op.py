#and
num1=30
num2=40
and_demo = num1==num2 and num1<num2 and num1!=0 and num2!=0 and num1>=num2
print("and:", and_demo)

and_demo= num1<num2 and num1!=0 and num2!=0 and num1<=num2
print("and:", and_demo)

#or

or_demo= num1==num2 or num1<num2 or num1!=0 or num2!=0 or num1>=num2
print("or:", or_demo)

or_demo= num1<num2 or num1!=0 or num2!=0 or num1<=num2
print("or:", or_demo)


or_demo= num1>num2 or num1!=30 or num2!=40 or num1>=num2
print("or:", or_demo)

#not
not_demo=not (num1>num2 or num1!=30 or num2!=40 or num1>=num2)
print("not_demo:", not_demo)

not_demo=not (num1<num2 or num1!=0 or num2!=0 or num1<=num2)
print("not_demo:", not_demo)