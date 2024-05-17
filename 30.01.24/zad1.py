plik= open('wyniki.txt','w')

a=int(input())
b=int(input())

for liczba in range(a,b):
    reszta= liczba%3
    if liczba %2==0:
        print(liczba,reszta,'parzysta', file=plik)
    else:
        print(liczba,reszta,'nieparzysta', file=plik)
plik.close()        
    
