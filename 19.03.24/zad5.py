plik= open('n_z.txt','r')
czyn1=[]
czyn2=[]
                                  
for linia in plik:
    czyn1=[]
    lista = linia.split()
    elem1=int(lista[0])
    elem2=int(lista[1])
    
    while elem1>1 :
        if elem1%2==0:
            elem1=elem1//2
            czyn1.append(elem1)
        
        elif elem1%3==0 or elem1%5==0:
            if elem1%3==0:
                elem1=elem1//3
                czyn1.append(elem1)

            elif elem1%5==0:
                elem1=elem1//5
                czyn1.append(elem1)
        
        else:
            czyn1.append(elem1)
            if len(czyn1)>1:
                if czyn1[-1]==czyn1[-2]:
                    czyn1.pop()
            #l. pierwsza        
            break
        
        
    print(czyn1)   