#Joseph Everden
#15/09/14
#Binary to hexadecimal

binary_value = int(input("Enter a 4 bit binary number: "))
if binary_value[0] == 1:
    bit4 = int(8)
else: bit4 = int(0)
if binary_value[1] == 1:
    bit3 = int(4)
else: bit3 = int(0)
if binary_value[2] == 1:
    bit2 = int(2)
else: bit2 = int(0)
if binary_value[3] == 1:
    bit1 = int(1)
else: bit1 = int(0)

denary_value = bit1 + bit2 + bit3 + bit4
if denary_value == 1:
    hex_string = "1"

        
