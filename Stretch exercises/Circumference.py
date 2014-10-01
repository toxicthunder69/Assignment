#Joseph Everden
#21/09/14
#Circumference of a Circle

import math
print("Enter the length in cm")
r = float(input("Radius of the circle: "))
circum = round(2 * math.pi * r, 2)
area = round(math.pi * r ** 2, 2)
print("The circumference of your circle is {}cm.".format(circum))
print("The area of your circle is {}cm sqrd.".format(area))
