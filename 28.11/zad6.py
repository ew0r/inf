plik=open('dane.txt','r')
p=0
count=0
a=0
b=0

for linia in plik:
    linia=linia.strip()
    x=list(linia)
    p=0
    a=0
    if b==6:
        count+=1
    for cyfra in x:
        if p==0:
            a+=int(cyfra)
            p+=1
        if a==int(cyfra):
            continue
        if int(cyfra)>a:
            a+=int(cyfra)
            b+=1
        if int(cyfra)<a:
            break
        
print(count)         
