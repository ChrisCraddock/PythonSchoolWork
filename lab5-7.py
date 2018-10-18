

classA = 20
classB = 15
classC = 10
def main():
    seatA = int(input('How many Class A seat were sold?:'))
    seatB = int(input('How many Class B seat were sold?:'))
    seatC = int(input('How many Class C seat were sold?:'))

    total = sum(seatA,seatB,seatC)
    print('The total ticket sales today are $',total, sep='')

def sum(num1,num2,num3):
    result = (num1*classA)+(num2*classB)+(num3*classC)
    return result

main()