
'''
Ask the user how many numbers to generate and use a random number generator fill the list, generate in range of 1-100.

Store the numbers in a list and then display the following:

1. the lowest number in the list

2. the highest number in the list

3. the total of the numbers in the list

4. the average of the numbers in the list
'''
import random

def main():
#Constants to start with
    smallest = 0
    largest = 0
    n = int(input("How may numbers (between 1-100) would you like to generate?: "))
    total = 0
    while n >= 101 or n <= 0:
      print(input("Invalid input:How may numbers (between 1-100) would you like to generate?: "))
    else:
      randomList = random.choices(range(1, 101), k=n)
    print(sorted(randomList))
#Sort from smallest to largest,and pop the first and last numbers in the list
    organized = sorted(randomList)
    total = sum(randomList)
    average = sum(randomList) / len(randomList)
    largest = organized.pop()
    smallest = organized.pop(0)
#Print Results
    print('The total of all the numbers are ',str(total))
    print('The average of all the numbers are ',str(format(average,'.2f')))
    print('The largest of all the numbers are ',str(largest))
    print('The smallest of all the numbers are ',str(smallest))

main()
