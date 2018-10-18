#ASK USER TO ENTER A DISTANCE IN KILOMETERS AND CONVERT INTO MILES
kilometers = int(input('Please enter the kilometers you wish to convert: '))

def convert():
    miles = format(kilometers * 0.6214,'.2f')
    print(kilometers,"converts to ",miles, " miles")

convert()
