#Carter Hicks
#12/12/17
#Gift

print "We are creating a database of toys to let you know the cost for the toys."
toy = raw_input("Please enter the name of the toy: ")
gift = ["lionel mega tracks","lil lockitz","bff necklace","xbox","hoverboard","iphone x"]
cost = [49.99, 34.99, 24.99, 249.00, 299.99, 649.99]

if toy.lower() in gift:
    i = gift.index(toy.lower())
    print "The cost of",toy.title(),"is $",cost[i]

else:
    print "Sorry your toy is not on the list"
    new = float(input("Please enter the cost of your toy: "))
    print "The cost of",toy.title(),"is $",new


    
