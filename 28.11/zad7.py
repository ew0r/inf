plik=open('dane.txt','r')
x=''
l1=''
l2=''
count=0

for linia in plik:
    linia=linia.strip()
    x=list(linia)
    z=0
    q=0   
    l2=''
    l1=''
    
    while z<2:
        l2+=x.pop()
        z+=1
    while q<2:
        l1+=x.pop(-3)
        q+=1
    if l1==l2:
        count+=1    

print(count)
