#Utwórz funkcję pisz_duże2(lili, X) pobierającą listę liczb oraz liczbę X. Funkcja wypisuje indeksy elementów > X.
lili=[1,2,3,4,5,6,7,55,9,10]
x=5


def pisz_duże(lili, x):
    b=0
    for a in lili:
        b+=1
        if a>x:
            print(b)
            
pisz_duże(lili, x)    
