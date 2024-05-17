plik=open('dane.txt','r')
a=0
l1=''
x=0
y=0
mcount=0

for linia in plik:
    if y!=0:
        y+=1

    if x==y:
        mcount+=1
    linia=linia.split()
    
    a=0
    y=0
    x=0
    l1=''
    for elem in linia:
        y+=1
        if a==0:
            l1+=elem
            a+=1
            x+=1
        if str(elem)==l1:
            x+=1
print(mcount)            

    
