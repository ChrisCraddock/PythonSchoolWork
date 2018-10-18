#Total Monthly Car Expenses

def main():
    loan = int(input('Please enter your loan payment each month: '))
    insurance = int(input('Please enter your insurance payment each month: '))
    gas = int(input('Please enter your gas payment each month: '))
    oil = int(input('Please enter your oil payment each month: '))
    tires = int(input('Please enter your tire payment each month: '))
    maint = int(input('Please enter your maintenance payment each month: '))

    total = sum(loan,insurance,gas,oil,tires,maint)
    yearly = total * 12
    print('Your total monthly car expenses are $',total)
    print('The total yearly cost for your car is $',yearly)

def sum(num1,num2,num3,num4,num5,num6):
    result = num1+num2+num3+num4+num5+num6
    return result

main()
