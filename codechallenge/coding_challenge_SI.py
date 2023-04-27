
#p=principal amount
#n=no:of years
#r=rate of interest
def fun(p,n,r):
    print("SI=pnr/100")
    return(p*n*r)/100
result=fun(500,10,5)
print("SI = " +str(result))