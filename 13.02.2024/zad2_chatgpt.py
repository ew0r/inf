liczba = 123451234
cyfry = str(liczba)
wynik = []

for cyfra in set(cyfry):
    if cyfry.count(cyfra) > 1:
        wynik.append(cyfra)

print("Cyfry występujące więcej niż raz:",','.join(wynik))