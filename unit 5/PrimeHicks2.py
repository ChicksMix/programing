#carter hicks
#prime

r = 101
count = 0
for divisee in range (2,r):
    prime = True
    for divisor in range (2, divisee):
        if divisee % divisor == 0:
            prime = False               
            break
    if prime:
        count +=1
        print str(count)+")", divisee 
        
    
