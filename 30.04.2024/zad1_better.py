i='333333333'
a=0
b=3
c=0
temp=0
lista=[]
for elem in i:
    temp=i[a:b]
    if len(temp)!=0:      #jak string pusty to nie przepuści 
        lista.append(temp)
        a+=3
        b+=3
for elem in lista:
    c+=int(elem)
print(c)    
    
