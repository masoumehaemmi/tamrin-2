import math

n_number = int (input(" enter a number :"))

li=[]


for i in range (n_number) :
       if i==0 or i == 1 :
               li.append(1)
       else :
               fibo = li[i - 1] + li [i - 2]
               li.append(fibo)       
print(li)              
       
                

