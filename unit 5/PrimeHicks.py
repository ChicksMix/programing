#Carter Hicks
#prime


s=25
c=0
p=1

for n in range(1,s+1):
    c=c+1
    print str(c)+"."
    for x in range(2,102):
        if x%n== 0:
            p=p+1
            x=p
            print(x)
                
       
        
        



