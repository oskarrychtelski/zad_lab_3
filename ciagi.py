def suma_ar(a,b,n):
    print (((a+b)/2)*n)

def suma_geo(a,q,n):
    if q!=1:
        return a*((1-pow(q,n))/(1-q))
    elif q==1:
        print (a*n)