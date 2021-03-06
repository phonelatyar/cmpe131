import math

def calculator (number1, number2, operator):
	''' Check the input operator from the user and 
		match with the correspond function operator
	'''	
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
		print(str(result)+"\n") # change the result into string to add new line at the end
		
def menu():
	''' Load the prompt to the user display and call the calculator function'''
	number1 = float(input("Enter the first number: "))
	number2 = float(input("Enter the second number : "))
	operator = input("Enter the operation: ")
	calculator (number1, number2, operator)

while True:	# to break or continue the calculator function
	menu()
	exit = (str(input("Do you wish to exit? ")))
	if exit == "y":
		break
	elif exit == "n":
		continue
