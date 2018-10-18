

'''
Lets user specify how many numbers should randomly be generated
'''

import random

def main():
#Local Variables
    filename = ''
    numberOfRandoms = 0
    randomNumber = 0
    
#Get file name as input from the user
    filename = input("Enter the name and type of the file to which results should be saved: ")
    
    numberOfRandoms = int(input("Enter the amount of random numbers: "))

#--- Lab requests the output file have a certain name so this overwrites the users name
    filename = "randomNumber.txt"

    outputFile = open(filename,'w')
    
    for counter in range (numberOfRandoms):
    
        randomNumber = random.randint(1,500)
        outputFile.write(str(randomNumber) + '\n')
        
    outputFile.close()
    
    print("Your numbers have been written and saved")
    
main()
