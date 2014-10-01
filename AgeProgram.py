age = int(input("How old are you: "))
if age >= 18:
    print("You can vote!")
else:
    vote_age = 18 - age
    print("You can't vote yet, only {} more years.".format(vote_age))
if age < 65:
    retire_age = 65 - age
    print("You can also retire in {} years.".format(retire_age))
