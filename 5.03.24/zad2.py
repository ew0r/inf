#Utwórz funkcję pisz_duże(lili, X) pobierającą listę liczb oraz liczbę X. Funkcja wypisuje wartości elementów > X.
lili=[1,2,3,4,5,6,7,8,9,10]
x=5

def pisz_duże(lili, x):
    for a in lili:
        if a>x:
            print(a)
            
pisz_duże(lili, x)    