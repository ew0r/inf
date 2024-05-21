plik=open('e43.txt','r')
licznik=0
lista=[]
liczniki=[]
for linia in plik:
    pusta=linia.split()
    lista.append(pusta)

count=0
for x in range(0,5):
    count=0
    for elem in lista:
        count+=int(elem[x])
        
    #print(count)
    liczniki.append(count)

liczniki2=liczniki.copy()
liczniki.sort()

x=(liczniki2.index(liczniki.pop()))
print(x+1)
        
    

    

