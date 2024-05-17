plik0=open('dane3.txt','r')
plik1=open('dane28.txt','r')
plik2=open('dane23.txt','r+')
count=0
a=0

for linia in plik0:
    linia=list(linia)
    for elem in linia:
        elen=list(elem)
        if elen!=[' ']:
            plik2.write(elem)
        else:
            plik2.write('\n')          

for linia in plik1:
    linia=list(linia)
    for elem in linia:
        elen=list(elem)
        if a==0:
            plik2.write('\n')
            a+=1
        if elen!=[' ']:
            plik2.write(elem)
        else:
            plik2.write('\n')
print(plik2.read())
plik0=open('dane23.txt','r')
for linia in plik0:
    count+=int(linia)
print(count)