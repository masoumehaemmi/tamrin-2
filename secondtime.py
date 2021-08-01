import math


clock = int (input(" enter a oclock :"))
minute = int (input(" enter a minute :"))
second = int (input( "enter a second :"))

while  clock > 12 or minute > 59 or second > 59 :
        print ("no more than 12 o'clock , no more than 59 minute , no more than 59 second , try again")
        clock = int (input(" enter a oclock :"))
        minute = int (input(" enter a minute :"))
        second = int (input( "enter a second :"))
    

print (clock ," :" ,minute , " :" , second , )
c = clock * 3600
m= minute * 60
s= c + m + second 

print (s)
    