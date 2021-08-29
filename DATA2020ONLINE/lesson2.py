#Github - create a github account at the end of the lesson
#Functions and control statements
#Why Functions?
# Widely used in most Frameworks
# Widely used in Objected Oriented Programming
# They devide your big code into smaller modules or blocks
# One function can a speciffic task

#create a conversion function
#amount in kes is a parameter
def converter(amount_in_kes):
    # convert the amount received to usd
    amount_in_usd = amount_in_kes/108
    return amount_in_usd

def payroll():
    basic_salary = 50000
    allowances = 2000
    deductions = 3000

    # Find gross pay
    gross_pay = basic_salary + allowances
    print('Gross Pay is KES', gross_pay)
    # convert gross pay to usd
    print('Gross in USD', converter(gross_pay))

    # Find net pay
    net_pay = gross_pay - deductions
    print('Net Pay is KES', net_pay)
    #convert the net pay in usd
    #NB: converter is returning
    print('Net Pay in USD is', converter(net_pay))


# call a function for it to run
payroll()


