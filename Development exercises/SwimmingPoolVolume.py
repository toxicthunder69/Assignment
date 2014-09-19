#Joseph Everden
#18/09/14
#Pool Volume

leng = float(input("Enter the length of the pool in meters: "))
width = float(input("Enter the width of the pool in meters: "))
deep_end = float(input("Enter the depth of the deep end in meters: "))
shallow_end = float(input("Enter the depth of the shallow end in meters: "))
deep_depth = deep_end - shallow_end

shallow = (leng * width) * shallow_end
deep = ((leng * width) * deep_depth) / 2

volume = format(shallow + deep, '.2f')

print("{0}m cubed of water is needed to fill your pool.".format(volume))
