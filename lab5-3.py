def main():
    replacement_cost = int(input('Please enter the replacement cost of the building: '))
    print(min_amount(replacement_cost))


def min_amount(replacement_cost):
    cover = replacement_cost- (replacement_cost * .80)
    return cover


main()