import math

second = int(input(" enter a second : "))

clock = second // 3600
minute = second % 60
second = minute - clock

print ( clock , ":" , minute , ":", second)