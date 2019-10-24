#Carter hicks
#outer and inner loop

for n in range(1,6):
    print str(n)+")",
    for x in range(1,n+1):
        if x < n:
            print str(x)+",",
        else:
            print str(x)
        
        
