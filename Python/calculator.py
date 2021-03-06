import math

def calculator (number1, number2, operator):
		if operator == "+":	
			result = number1 + number2
		elif operator == "-":	
			result = number1 - number2
		elif operator == "*":	
			result = number1 * number2
		elif operator == "/":	
			result = number1 / number2
		elif operator == "//":	
			result = number1 // number2
		elif operator == "**":	
			result = number1 ** number2
		print(str(result)+"\n")
		
def menu():
	number1 = float(input("Enter the first number: "))
	number2 = float(input("Enter the second number : "))
	operator = input("Enter the operation: ")
	calculator (number1, number2, operator)

while True:
	menu()
	exit = (str(input("Do you wish to exit? ")))
	if exit == "y":
		break
	elif exit == "n":
		continue
