



def main():
    f,l,sal= enter()
   
    
    if sal>=40000:
        ns=morethan40(sal)
       
    else:
        ns=lessthan40(sal)
    
    
    output(f,l,ns)

def enter():
    f= raw_input("Enter your first name: ")
    l= raw_input("Enter your last name: ")
    sal= float(input("Enter your annual salary: "))
    return f,l,sal

def morethan40(sal):
    return ((sal-40000)*.02)+2000+sal


def lessthan40(sal):
    return (sal*.05)+sal
    


def output(f,l,ns):
    print "The new salery for",(f),(l),"is: ",ns

main()
