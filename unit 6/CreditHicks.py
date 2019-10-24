#credit card

def main():
    ob= float(input("Enter the old balance: "))
    cm= float(input("Enter charges for the month: "))
    cred=float(input("Enter any credits: "))
    print "The new balance is: ",newBalance(ob,cm,cred)
    print "The minimum payment is: ",minimumPayment(newBalance(ob,cm,cred))


def newBalance(ob,cm,cred):
    newBalance= (cm - cred) + ob + (.015*ob)
    return newBalance


def minimumPayment(newBalance):
    if newBalance<=20.00:
        minimumPayment = newBalance
        return minimumPayment
    
    else:
        minimumPayment =float(20.00 + ((newBalance - 20.00)* .10))
        return minimumPayment
main()
