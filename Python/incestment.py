import math



checker1 = False
checker2 = False
checker3 = False

while not checker1:
	principal = input("Enter the starting amount : ")
	if principal.isdigit():
		checker1 = True
		
	else: 
		print("False")
		

while not checker2:
	interest_rate_user = input("Enter the interest rate in percentage: ")
	if interest_rate_user.isdigit():	
		checker2 = True
		
	else: 
		print("False")
		

while not checker3:
	years = input("Enter the number of years: ")
	if years.isdigit():
		checker3 = True
		
	else: 
		print("False")
		

principal = float(principal)
interest_rate_user = float(interest_rate_user)
years = float(years)


interest_rate = interest_rate_user / 100


def calculate_apr(principal, interest_rate, years):
	initial_years = 0
	while initial_years != years:
			total_amount = principal*(1+interest_rate)
			principal = total_amount
			initial_years = initial_years + 1

	print("Total money after " + str(years) +" years is " + str(total_amount))

calculate_apr(principal, interest_rate, years)


