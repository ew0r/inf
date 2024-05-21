plik=open('e43.txt','r')
licznik=0
lista=[]
trash=[]
for linia in plik:
    pusta=linia.split()
    lista.append(pusta)
    licznik=0
    for elem in pusta:
        licznik+=int(elem)
    trash.append(licznik)
trash2=trash.copy()
trash.sort()

x=(trash2.index(trash.pop()))
print(x+1)