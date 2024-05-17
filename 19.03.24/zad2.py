plik=open('n_z.txt','r')
mcount=[]
mcount2=[]
icount=0
a=1
b=1
for linia in plik:
    linia=linia.strip()
    if a!=1:
        mcount.append(icount)
    icount=0
    for elem in linia:
        a-=1
        if elem != ' ':
            icount+=int(elem)
            
mcount.append(icount)
mcount2=mcount.copy()
mcount2.sort()
maxsum=mcount2.pop()

for elem1 in mcount:
    if int(elem1)==maxsum:
        print('Index lini o największej sumie cyfr to',b)
    b+=1
print('A ta suma to',maxsum)        
        