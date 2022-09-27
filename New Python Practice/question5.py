unit = int(input("Enter the unit consumed :\n"))
total = 0
if unit<= 50:
    total = unit*0.5
elif unit <=150:
    total = (50*0.5) + ((unit - 50)*0.75)
elif unit <=250:
    total = (50*0.5) + (100*0.75) + ((unit-150) *1.2)
else :
    total = (50 * 0.5) + (100*0.75) + (100 *1.2) + ((unit-250) *1.5)


total = total + (total *20 / 100)

print("Number of unit Consumed :" , unit)
print("Total Bill                          : Rs", total)


