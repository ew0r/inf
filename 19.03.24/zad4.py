plik=open('n_z.txt','r')
dzielniki1=[]
dzielniki2=[]
mainlist=[]

for linia in plik:
    mainlist=[]
    dzielniki1=[]
    dzielniki2=[]
    lista = linia.split()
    elem1=int(lista[0])
    elem2=int(lista[1])
    
    for a in range(1,elem1+1):
        if elem1%a==0:
            dzielniki1.append(a)
    
    for a in range(1,elem2+1):
        if elem2%a==0:
            dzielniki2.append(a)
            
    for a in dzielniki1:
        for b in dzielniki2:
            if a==b:
                mainlist.append(b)
    print(mainlist.pop())            
