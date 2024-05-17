#policz średnią wagę dla mężczyzn i dla kobiet
plik=open("ludzie.txt", 'r', encoding='utf-8')
m=0
k=0
wagam=0
wagak=0

for linia in plik:
    linia=linia.split()
    if linia[4]== 'M':
        m+=1
        wagam+=int(linia[5])
    if linia[4]== 'K':
        k+=1
        wagak+=int(linia[5])

print('Średnia waga kobiet =',wagak/k,'kg')
print('Średnia waga mężczyzn =',wagam/m,'kg')