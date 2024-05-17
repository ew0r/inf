plik=open('dane.txt','r')

for linia in plik:
    ones= int(linia) % 10
    thousands = (int(linia) % 10000)//1000
    if thousands > ones:
        print(linia.strip())

# Wypisz liczby, gdzie cyfra tysięcy jest > cyf. jedności

