i='123 456 992'
lista=i.split()
temp=0
sumy=[]
a=0
for elem in lista:
    if a>0:
        sumy.append(temp)
        temp=0
    for cyfra in elem:
        temp+=int(cyfra)
    a+=1
    if temp%2==0:
        print(elem)
    