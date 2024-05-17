plik=open('dane.txt','r')

for linia in plik:
    dno= int(linia) % 10
    if dno < 3:
        print(linia.strip())

# Wypisz liczby gdzie cyfra jedności jest < 3