#Carter Hicks
#Salary

def main():
    sal=10
    sal2=1
    print "You are offered two salary options for ten days of work."
    print "\nOption 1:"
    print "$100.00 per day for 10 days"
    print "\nOption 2:"
    print "$1.00 for the first day"
    print "$2.00 for the second day"
    print "$4.00 for the third day"
    print "Continued the pattern of doubling each day for the 10 days"
    print "Choose an option"
    ssal= Option1(sal)
    ssal2=Option2(sal2)
    print "Option 1: the salary will be $",Option1(ssal)
    print "Option 2: the salary will be $",Option2(ssal2)
    if  Option1(ssal)> Option2(ssal2):
        print "Option 1 is a better deal for you"
    elif Option1(ssal) < Option2(ssal2):
        print "Option 2 is a better deal for you"
    else:
        print "Both options are equal to each other"



def Option1(sal):
    sal=10
    ssal=sal*100
    return ssal

def Option2(sal2):
    mi=1
    while mi >=10:
        ans= sal2*sal2
        sal2= sal2+sal2
        mi=mi+1
        ssal= ans+sal2
    return ssal2

main()


    
