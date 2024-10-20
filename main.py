def calculate_paye(salary):
    # Tax brackets
    first_bracket = 150000
    second_bracket = 350000
    third_bracket = 2050000

    # Tax rates
    second_bracket_rate = 0.25
    third_bracket_rate = 0.30
    fourth_bracket_rate = 0.35

    # PAYE calculation
    if salary <= first_bracket:
        paye = 0
    elif salary <= first_bracket + second_bracket:
        paye = (salary - first_bracket) * second_bracket_rate
    elif salary <= first_bracket + second_bracket + third_bracket:
        paye = (second_bracket * second_bracket_rate) + \
               (salary - first_bracket - second_bracket) * third_bracket_rate
    else:
        paye = (second_bracket * second_bracket_rate) + \
               (third_bracket * third_bracket_rate) + \
               (salary - first_bracket - second_bracket - third_bracket) * fourth_bracket_rate
    
    return paye

print("Enter Currency Symbol:", end=" ")
symbol = input()
print("Enter q, quite or exit to end the program\n")
while(True):
	print("Enter Your Salary:", end=" ")
	salary = input()
	if salary.lower()=="q" or salary.lower()=="quite" or salary.lower()=="exit":
		print("Thanks for using our system")
		break
	try:
		salary = float(salary.replace(",", ""))
		paye = calculate_paye(salary)
		print(f"Salary: {symbol}{salary:,.2f} Tax: {symbol}{paye:,.2f} Remaining: {symbol}{(salary-paye):,.2f}")
	except:
		print("Check your input and try again")

