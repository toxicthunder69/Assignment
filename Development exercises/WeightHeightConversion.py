#Joseph Everden
#18/09/14
#Height and Weight Conversion

height_inch = int(input("Enter your height in inches: "))
weight_stone = int(input("Enter your weight in stones: "))

height_cm = height_inch * 2.45
weight_kg = weight_stone * 6.364

print("You are {0}cm tall and you weight {1}kg.".format(height_cm, weight_kg))
