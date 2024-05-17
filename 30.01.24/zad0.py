plik= open('wyniki.txt','w')
for x in range (1,100+1):
    print(x, 'to liczba', file=plik)
plik.close()    