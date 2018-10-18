

'''
A program that calculates the number of packages of hot dogs and the number
of packages of buns needed for a cookout, with the minimum amount of leftovers.
'''
#--Input
GUESTS = int(input('Enter the number of people attending the cookout: '))
HOTDOGS = int(input('Enter the number of hot dogs each person will be given: '))

#--Constants
hotdog_pack = 10
hotdog_buns = 8

#-Calculations
HD_needed = GUESTS * HOTDOGS
HD_packs = HD_needed / hotdog_pack
Buns_needed = HD_needed / hotdog_buns
HD_left = ((HD_needed // hotdog_pack) * hotdog_pack + hotdog_pack) - HD_needed
Buns_Left = ((HD_needed // hotdog_buns) * hotdog_buns + hotdog_buns) - HD_needed
zero_HD_left = HD_needed % hotdog_pack
zero_Buns_left = HD_needed % hotdog_buns

#---Output
#calculate the minimum hotdog packages:
if zero_HD_left > 0:
  print("Minimum hot dog packages required:", int(HD_packs) + 1)
else:
  print("Minimum hot dog packages required:", int(HD_packs))
#calculate the minimum bun packages:
if zero_Buns_left > 0:
  print("Minimum hot dog buns packages required:", int(Buns_needed) + 1)
else:
  print("Minimum hot dog buns packages required:", int(Buns_needed))
#calculate leftovers:
if zero_HD_left > 0:
  print("Hot dogs that will be left over:", int(HD_left))
else:
  print("Hot dogs that will be left over:", int(zero_HD_left))
if zero_Buns_left > 0:
  print("Hot dog buns that will be left over:", int(Buns_Left))
else:
  print("Hot dog buns that will be left over:", int(zero_Buns_left))
