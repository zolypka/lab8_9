import math
n = int(input("enter the number of the fibonacci number: "))
a = int((((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)/math.sqrt(5))
print (a)