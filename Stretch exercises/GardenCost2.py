#Joseph Everden
#11/09/14
#Stretch Exercise

leng = 0
width = 0
border_input = 0
border = 0
turf = 0
leng_start = True
width_start = True
print("Enter the measurements of you garden in meters")

while leng <= border or width <= border:
    if leng <= border:
        if leng_start == True:
            leng = float(input("Length of your garden: "))
            leng_start = False
        else:
            print("Your garden isn't long enough for a {0}m border around it.".format(border_input))
            leng = float(input("Length of your garden: "))
    if width <= border:
        if width_start == True:
            width = float(input("Width of your garden: "))
            width_start = False
        else:
            print("Your garden isn't wide enough for a {0}m border around it.".format(border_input))
            width = float(input("Width of your garden: "))
    
    if border == 0:
        border_input = float(input("Enter the desired border size: "))
        border = border_input * 2
    else: break
    if turf == 0:
        turf = float(input("Enter price per sqrm of turf in £'s: "))
    else: break

area = (leng - border) * (width - border)
cost = format(area * turf, '.2f')

print("It will cost you £{0} to turf your garden if you have a {1}m border around it.".format(cost, border_input))

