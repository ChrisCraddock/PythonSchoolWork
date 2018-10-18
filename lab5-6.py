#Get input for calories from fat
#Get calories from carbs

def main():
    fat = int(input('Enter your daily amount of Fat grams: '))
    carbs = int(input('Enter your daily amount of Carb grams: '))
    fat_cal(fat)
    carb_cal(carbs)

def fat_cal(fat):
    calories = fat * 9
    print('Your daily calories from fat are: ',calories,'calories')

def carb_cal(carbs):
    calories = carbs * 4
    print('Your daily calories from carbs are: ',calories,'calories')

main()