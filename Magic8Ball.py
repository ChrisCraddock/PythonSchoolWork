
import random
'''
Use a random number generator to determine the answer, from the attached file, to each question.

Read the answer list from the file provided and put them into your list.
'''
def main():
  with open('8_ball_responses.txt','r') as q:     #Open the 8 ball file
    answers = [line.strip() for line in q]        #Put the contents into a list

  print(input('What question do you have that needs an answer?: '))
  print(random.choice(answers))
  ask_again = input('Do you have another question? [Y/N]')    #Ask question and exit if user is finished
  if ask_again == 'Y':
      main()
  elif ask_again == 'y':
      main()
  else:
    exit()

main()
