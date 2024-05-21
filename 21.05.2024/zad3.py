plik=open('e43.txt','r')
licznik=0
lista=[]
for linia in plik:
    pusta=linia.split()
    lista.append(pusta)

count=0
for x in range(1,5):
    count=0
    for elem in lista:
        count+=int(elem[x])
    
    print(count)

        
    

    
