import math
a = int(input("first number :  "))
op = input("enter a operator : ")
b = int(input("second number : "))
if op == "+":
	print(a + b)
elif op == "-":
	print(a - b)
elif op == "*":
	print(a * b)
elif op == "/":
	if b != 0:
		print(a / b)
	else:
		print("undefined")
else:
	print("wrong operator")
