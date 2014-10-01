#Joseph Everden
#21/09/14
#Circular Pool

import math
print("Enter lengths of your pool in cm's")
r = float(input("Diameter of pool: ")) / 2
dep = float(input("Depth of pool: "))
vol = round((math.pi * r ** 2) * dep, 2)
print("Your pool can hold {0}cm cubed of water.".format(vol))
