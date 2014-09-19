#Joseph Everden
#18/09/14
#Remainder Division

num1 = int(input("Enter the number to be divided: "))
num2 = int(input("Enter the number to divide by: "))

whole_num = num1 // num2
remainder_num = num1 % num2

print("The answer is {0} remainder {1}".format(whole_num, remainder_num))
