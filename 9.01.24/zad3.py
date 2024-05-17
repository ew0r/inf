plik=open('dane.txt','r')

for linia in plik:
    ones= int(linia) % 10
    tens= (int(linia) % 100)//10
    if (ones+tens)<10:
        print(linia.strip())

# Wypisz liczby gdzie suma cyf.dziesiątek i cyf. jedności < 10

