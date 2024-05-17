x=str(input())
lst=list(x)
co=len(lst)
a=1
b=1
l1=''
l2=''

for z in lst:
    a+=1
    if a<co:
        if b==1:
            l1+=z
            b-=1
    if a==co+1:
        l2+=z

if l1==l2:
    print('tak')
else:
    print('nie')
    
