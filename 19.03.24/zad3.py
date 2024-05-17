plik=open('n_z.txt','r')
count=0

for linia in plik:
    lista = linia.split()
    suma=0
    count=0
    suma=int(lista[0])+int(lista[1])
    
    
    for a in range(1,suma+1):
        if suma%a==0:
            count+=1
    if count<=2:
        print(lista)

        
