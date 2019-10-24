#Carter Hicks
#1/17/18


hi= 0
lo= 300
s=0.0
t=0.0
c=0.0
while s<>-1:
    s=float(input("Enter a score or -1 to stop: "))
    if s<>-1:
        t=t+s
        c=c+1
        if s > hi: #Test for high score
            hi = s
            
        if s< lo: #Test for low score
            lo =s
            
a=t/c
print "The average score is: ",a        
print "The highest score is: ",hi
print "The Lowest score is: ",lo
