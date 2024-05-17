n= int(input())
cf=[1,1]
a=1

nl=list(str(n))
lc=len(nl)

lcn=len(list(str(n)))

while lc>=lcn:
    l=cf[-1] + cf[-2]
    cf.append(l)
    lcn=len(list(str(cf[-1])))

cf.pop()
print(cf)
