#Utwórz funkcję stop(lili, X). Funkcja wypisuje elementy dopóki ich indeks jest < X.
lili=[1,22,3,4,5,6,7,55,9,10]
lilix=[]
x=5

def stop(lili, x):
    b=0
    for a in lili:
        b+=1
        if b<x:
            lilix.append(a)
    return(lilix)        
stop(lili, x)
print(lilix)

