plik=open('e43.txt','r')
licznik=0
lista=[]
for linia in plik:
    pusta=linia.split()
    lista.append(pusta)
    for elem in pusta:
        licznik+=int(elem)
print(licznik)    

    