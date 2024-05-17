plik0=open('dane3.txt','r')
plik1=open('dane28.txt','r')
plik2=open('wyniki.txt','w')
plik3=open('dane23.txt','w')

for linia in plik0:
    linia=list(linia)
    for elem in linia:
        elen=list(elem)
        if elen!=[' ']:
            plik3.write(elem)
        else:
            plik3.write('\n')
            
plik3=open('dane23.txt','r')            
for linia in plik3:
    if int(linia)%3==0:
       plik2.write(linia)

plik3=open('dane23.txt','w')       
for linia in plik1:
    linia=list(linia)
    for elem in linia:
        elen=list(elem)
        if elen!=[' ']:
            plik3.write(elem)
        else:
            plik3.write('\n')        

plik3=open('dane23.txt','r')            
for linia in plik3:
    if int(linia)%2==0:
       plik2.write(linia)

plik3.close()
plik2.close()
#czemu to się dodaje od nowej lini ?
#plik został ponownie otwarty więc zaczyna zapisywać od nowej wolnej lini)
