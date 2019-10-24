#Carter Hicks
import random

h= 50
l=1
c=1
ans=random.randrange(l,h)
num=int(input("Guess a number between 1 and 50: "))
while num<>ans:
    if num>ans:
        num=int(input("Incorrectnter a lower value :"))
    else:
        num=int(input("Incorrect enter a higher value :"))
    c=c+1
print "Correct the number was",ans,"it took you",c,"guesses"
