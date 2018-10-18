

"""
The problem is to write a program that will ask the user to enter
the amount of a purchase.  The program should then compute the
state and county sales tax.  Afterwards, the program should display
the amount of the purchase, the state tax, county tax, total sales
tax, and the total of the sale.
"""

# Input
original_price = float(input('What is the price of the item? : '))  # Get the starting price

STATE_TAX = 0.05  # State tax for 5%
COUNTY_TAX = 0.025  # County tax for 2.5%

# Processing
State_Price = original_price * STATE_TAX  # Find the price of state tax
County_Price = original_price * COUNTY_TAX  # Find the price of county tax
Final_Price = original_price + State_Price + County_Price  # Find the final price after adding the tax

# Output
print('Price before taxes: $', format(original_price, ',.2f'), sep='')  # Print the original price
print('State Tax: ', format(STATE_TAX, '.0%'))  # Print the state tax amount
print('County Tax: ', format(COUNTY_TAX, '.1%'))  # Print the county tax amount
print('Total Tax: $', format(State_Price + County_Price, ',.2f'), sep='')  # Print total tax amount
print('Price after taxes: $', format(Final_Price, ',.2f'), sep='')  # Print the final price after tax
