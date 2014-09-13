#Joseph Everden
#11/09/14
#Stretch Exercise

print("Enter the measurements of you garden in meters")
leng = float(input("Length of your garden: "))
width = float(input("Width of your garden: "))
turf = int(10)
border = int(2)

if leng <= border or width <= border:
    print("Your garden isn't big enough to turf with a 1 meter border.")
else:
    turf_leng = leng - border
    turf_width = width - border
    area = turf_leng * turf_width
    cost = format(area * turf, '.2f')
    
    print("It will cost you £{0} to turf your garden.".format(cost))
