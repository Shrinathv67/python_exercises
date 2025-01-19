"""
Prompt the user to enter the annual income. 
All income above 500000 is taxed at 10%.
Print the tax.

"""

ann_income = int(input("Please enter the annual income: "))
tax_income = ann_income - 500_000
if tax_income > 0:
    tax = tax_income*(10/100)
    print(tax)
else:
    print("No tax")


