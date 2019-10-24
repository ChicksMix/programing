#Carter Hicks
#1/12/18

n=0.0
t=0.0
c=0.0
while n<>-1:
    n=float(input("Enter a score or -1 to stop: "))
    if n<>-1:
        t=t+n
        c=c+1

a=round(t/c,2)
print "Your average score is",a
