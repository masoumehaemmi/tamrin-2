import math



count = int( input(" enter a number of student :"))

grade = []

for i in range(count) :
   lesson = float(input(" enter programming scores :"))
   grade.append( lesson)
a = sum (grade)
ave = a / count
print (" average :" , ave)

m = max (grade)
print ("max :" , m)

mi = min (grade)
print (" min :" , mi)


