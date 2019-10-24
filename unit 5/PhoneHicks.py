#Carter Hicks
#phone number


p=raw_input("Enter a phone number with hyphen separators: ")
pn=[]

for n in p:
    if n <>"-":
        pn.append(n)
print "Number without - "
for index in range(len(pn)):
    print pn[index],
