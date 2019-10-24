#Carter Hicks
#12/14/17
#new year


resolution =["exercise more", "lose weight", "eat healthier", "stop smoking", "more family time"]
broken = ["lose weight", "stop smoking", "eat healthier", "more family time", "save money"]

res1 = raw_input("Enter your New Year's Resolution: ")

if res1.lower() in resolution:
    if res1.lower() in broken:
        print res1,"is both one of top 5 made resolution and broken resolution"
    else:
        print res1,"is one of the top 5 made resolution"
elif res1.lower() in broken:
    print res1,"is one of the top 5 made broken resolution"
else:
    print "Your resolution was not top 5 made resolution or broken."
    print "It has been added to the resolution list."
    resolution.append(res1)
    

