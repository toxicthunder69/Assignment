#Joseph Everden
#15/09/14
#Denary to binary

denary_value = int(input("Enter a denary number: "))
binary_string = ""
while denary_value > 0:
    binary_string = str(denary_value % 2) + binary_string
    denary_value = denary_value // 2
    
print("The binary equivalent is ", binary_string)
