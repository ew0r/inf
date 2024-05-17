p=str(input())
x=list(p)
c=len(x)
q=0
a=0
count=0
prt1=''     
prt2=''

if c==1 or c==2 or p=='':
    q+=2

while q<2:
        prt1+=x.pop()
        q+=1

while x!=[]:
    if prt1==prt2:
        count+=1
    a=0
    prt2=''
    while a<2:
        if x!=[]:
            prt2+=x.pop()
            a+=1
        else:
            break

if prt1==prt2:
    count+=1
count+=1

if c/2==count:
    print('tak')
else:
    print('nie')