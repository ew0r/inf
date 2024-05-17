plik=open('dane.txt','r')
z=0
count=0

for linia in plik:
    linia=linia.strip()
    x=list(linia)
    if z==30:
        count+=1
    z=0                
    for cyfra in x:
        z+=int(cyfra)
print(count)         
