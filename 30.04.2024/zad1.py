i='111111111' 
lista=[]
wait=''
a=0
suma=0
for elem in i:
    wait=wait+elem
    if a%3==2:
        lista.append(wait)
        wait=''
    a+=1
    
for elem in lista:
    suma+=int(elem)
print(suma)    