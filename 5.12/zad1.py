plik=open('dane3.txt','r')
plik2=open('dane23.txt','w')
count=0

for linia in plik:
    linia=list(linia)
    for elem in linia:
        elen=list(elem)
        if elen!=[' ']:
            plik2.write(elem)
        else:
            plik2.write('\n')          
plik.close()

plik2=open('dane23.txt','r')
for linia in plik2:
    linia=linia.strip()
    if int(linia)%2==1:
        count+=1
print(count)    