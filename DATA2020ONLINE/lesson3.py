#declare variables to store gross income, and nuber of children
# Each taxpayer's tax due is computed as follows:
#The taxpayer's dependency exemption is determined by multiplying $3000 by the number of children.
#The taxpayer's net income is determined by taking the taxpayer's gross income and
# subtracting the taxpayer's dependency exemption
# if net pay is less than 50000, tax is 15%of salary
#   50000 - 70000, tax is 20% of salary
#   over 70000 pay 25% 0f salary
def check(net_income):# Expecting the net income to be brought in
    if net_income < 50000:
        print('Tax will be 15% of', net_income)
    elif net_income < 70000:
        print('Tax will be 20% of', net_income)
    elif net_income > 70000:
        print('Tax will be 25% of', net_income)
    else:
        print('Tax will be 30% of', net_income)

def employee_tax():
    gross_income = 50000
    number_of_children = 2

    #get dependency exemption
    dependency_exemption = number_of_children * 3000
    print('Dependency Exemption =', dependency_exemption)

    net_income = gross_income - dependency_exemption
    print('Net Income KES =',net_income)

    # Re use a function in lesson2
    from lesson2 import converter
    print('Net Icome in USD', converter(net_income))

    #Here we learn that code is improved when functions are used. i.e converter reused
    #DRY - Dont Repeat Yourself
    #control statement
    check(net_income) #provides the net income to check()

employee_tax()