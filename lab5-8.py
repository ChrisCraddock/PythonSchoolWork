

#250 sq ft coverage = 1 gal and 8 hr labor
#Price = $35/hr
#Ask the user to enter:
#   -the square feet of wall space to be painted
#   -the price per gallon of paint
#Display:
#   -number of gal required
#   -hours of labor required
#   -total paint cost
#   -labor charges
#   -total project cost


#-----MAIN LOOP---#
def main():
    user_wall = int(input("Please enter the sq feet of wall"+
                             "needing to be covered: "))
    user_paint = float(input("Please enter the price of paint"+
                             "per gallon: (nearest whole dollar) $"))
    gallons_need = paint_needed(user_wall)
    hours_needed = get_hours(user_wall)
    paint_cost = int(user_paint * gallons_need)
    labor_cost = int(gallons_need * 35)
    total_cost = int(paint_cost + labor_cost)
    print("The total cost of paint is: $",paint_cost, sep='')
    print("The total cost for labor at $35/hour is: $",labor_cost, sep='')
    print('The total project cost is: $',total_cost, sep='')


#-----FUNCTIONS FOR MAIN LOOP---#
def paint_needed(gallons):
    paint = gallons / 250
    more_paint = gallons % 250
    if more_paint > 0:
        print("The number of gallons of paint required are: ", int(paint + 1), "gallons")
        return paint + 1
    else:
        print("The number of gallons of paint required are: ",paint, "gallons")
    return paint


def get_hours(user_wall):
    hours = (user_wall / 250) * 8
    more_hours = (user_wall % 250) * 8
    if more_hours > 0:
        print("The total hours of labor required are: ", int(hours + 1),"hours")
        return hours + 1
    else:
        print("The total hours of labor required are: ", hours, "hours")
    return hours


main()