n=int(input())
n=list(str(n))
ls=[]
cf=[1,1,2]
a=1

while cf[-1]<100000:
    l=cf[-1] + cf[-2]
    cf.append(l)
    
    for a in cf:
        for b in n:
            if str(a)==b:
                ls.append(cf[-1])
                next

print(ls)