# property tax is 0.72 for each $100.  $6000 will be $43.20 in taxes

def main():
    property_value = int(input('What is the value of the property? : '))
    print('The assessed value is $', format(assValue(property_value), '.2f'))
    print('The property tax is $', format(propTax(assValue(property_value)), '.2f'))


def assValue(property_value):
    value = property_value * 0.60
    return value


def propTax(value):
    pt = (value / 100) * 0.72
    return pt


main()
