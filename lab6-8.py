
'''
Write a program that :
    reads random numbers from a file
    displays the numbers
    displays the sum if the numbers
    the total random numbers
'''
import random

def main():
  #Opens File
  infile = open('randomNumber.txt', 'r')
  amount = 0
  total = 0
  #Reads and Totals numbers
  print("The random numbers are: ")
  for line in infile:
        amount = int(line)
        total += amount
        print(line)

  infile.close()

  print("The total of the numbers = ", total)
  print("The number of the random numbers read from the file = "+str())
  
main()