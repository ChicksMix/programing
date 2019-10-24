



def main():
    n1=int(input("Enter a whole number: "))
    n2=int(input("Enter a second whole number: "))
    print "The average of the two numbers is",average(n1,n2)
    print "The highest of the two numbers is",high(n1,n2)
    print "The highest number to the power to the lowest number is",power(n1,n2)

def average(n1,n2):
    avg=n1+n2/2
    return avg
        
        
def high(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def power(n1,n2):
    if n1 > n2:
        return n1**n2
        
    elif n1< n2:
        return n2**n1
    else:
        return n1**n2

main()
