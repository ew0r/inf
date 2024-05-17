plik=open('dane.txt','r')

for linia in plik:
    half= int(linia) % 100
    half2= (int(linia)%10000)//100
    if half>half2:
        print(linia.strip())

# Wypisz liczby,  gdzie pierwsza połówka jest > drugiej połówki



