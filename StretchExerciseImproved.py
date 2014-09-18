#Joseph Everden
#11/09/14
#Stretch Exercise

while :
    print("Enter the measurements of you garden in meters")
    leng = float(input("Length of your garden: "))
    width = float(input("Width of your garden: "))
    border_input = float(input("Enter the desired border size: "))
    border = border_input * 2
    turf = 10
    
    if leng <= border:
        print("The length of your garden isn't long enough for a {0}m border.".format(border))
        leng = float(input("Length of your garden: "))
    if width <= border:
        print("The width of your garden isn't long enough for a {0}m border.".format(border))
        width = float(input("Width of your garden: "))

turf_leng = leng - border
turf_width = width - border
area = turf_leng * turf_width
cost = format(area * turf, '.2f')

print("It will cost you £{0} to turf your garden.".format(cost))
