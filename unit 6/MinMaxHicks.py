#Carter Hicks
#min/max

def main():
    numlist= [4,78,38,5,1,88,25,96,-8,42,44,43]
    mi= minF(numlist)
    ma= maxF(numlist)
    print "\nThe lowest value is: "+str(mi)
    print "\nThe highest value is: "+str(ma)

def maxF(numlist):
    ma=numlist[0]
    for num1 in numlist:
        if num1> ma:
            ma= num1
    return ma




def minF(numlist):
    mi=numlist[0]
    for num in numlist:
        if num < mi:
            mi= num
    return mi

main()
