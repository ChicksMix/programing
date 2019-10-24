#Mortgage


def main():
    ar,mop,bm= enter()
    intp,redp,emb= cal(ar,mop,bm)
    dis(intp,redp,emb)
    

def enter():
    ar=float(input("Enter annual rate of interest: "))
    mop= float(input("Enter monthly payment: "))
    bm= float(input("Enter beginning of the month: "))
    return ar,mop,bm
    


def cal(ar,mop,bm):
    if ar <=1:
        far=ar
    else:
        far=ar/100
    mri= (far/12)
    intp= round(bm*mri,2)
    redp=round(mop-intp,2)
    emb=round(bm-redp,2)
    return intp,redp,emb

def dis(intp,redp,emb):
    print "Interest paid for the month:	",intp
    print "Reduction of principal: ",redp
    print "End of month balance: ",emb



main()
