import random

tas_number = random.randint(1,6)

print("tas_number :" , tas_number)

if tas_number == 6 :
    tas_number = random.randint(1,6)
    print (" you have a prize")

    print("tas_number :" , tas_number)

else:
    print ("end")



