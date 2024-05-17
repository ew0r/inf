plik=open('dane.txt','r')
l1=0
l2=0
l3=0
mcount=0
mcount2=0
for linia in plik:
    if l1==l2:
        mcount+=1
    if l3==l2:
        mcount2+=1
    linia=linia.split()  
    l1=0
    l2=0
    l3=0
    for elem in linia:
        l2+=1
        if int(elem)%2==0:
            l1+=1
        if int(elem)%2==1:
            l3+=1
print("Parzyste =",mcount)
print("Nieparzyste =",mcount2)