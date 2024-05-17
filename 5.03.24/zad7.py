#Utwórz funkcję pomiń(lili, X). Funkcja zwraca listę zawierającą liczby z lili, ale pomija liczby podzielne przez X.
lili=[1,2,3,4,5,6,7,55,9,10]
lilix=[]
x=5


def pomiń(lili, x):
    for a in lili:
        if a%x!=0:
            lilix.append(a)
            
pomiń(lili, x)
print(lilix)

