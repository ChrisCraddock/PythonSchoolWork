

'''
This program will do the following:
1. Ask for input of the amount of organisms
2. Ask for input of the daily population increase in percent
3. Ask for input of the maximum days the organism multiplies
4. Calculate the total population per day
5. Print the results for each day
'''

# ===Begin Loop
while True:
    ORGANISMS = int(input("How many organisms do you want to start with?: "))
    if ORGANISMS == 0:
        print("You must have atleast 1 organism")
        quit()
    else:
# ===Input
        INCREASE = float(input("At what percent (10% = 0.10) should they increase at?: "))
        DAYS = int(input("How many days should the be left to multiply?: "))
        population = ORGANISMS
        print()
        print('Days\tPopulation')
        print('------------------')
    break
# ===Process
for currentDay in range(1, DAYS + 1):
    print(currentDay, "\t", format(population, ',.3f'))
    population = population + (INCREASE * population)
