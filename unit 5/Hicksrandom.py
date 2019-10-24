#Carter Hicks
#1/19/18
import random



h= int(input("Enter the highest possible value for the number: "))
l= int(input("Enter the lowest possible value for the number: "))
num1 = 0
num2 = 0
num3 = 0

while num1== num2 or num1== num3 or num2 == num3 :
    num1 = random.randrange(l,h)
    num2 = random.randrange(l,h)
    num3 = random.randrange(l,h)


print num1,",",num2,",",num3
    
        
 
