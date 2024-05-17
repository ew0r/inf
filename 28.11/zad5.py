plik=open('dane.txt','r')
p=0
z=''
count=0
a=0

for linia in plik:
    linia=linia.strip()
    x=list(linia)
    if a==6:
        count+=1
    a=0
    p=0
    z=''
    for cyfra in x:
        if p==0:
            z+=cyfra
            p+=1
        if cyfra==z:
            a+=1
print(count)         