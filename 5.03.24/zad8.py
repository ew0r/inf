#Utwórz funkcję scal_x(lili1, lili2, x). Funkcja zwraca listę zawierającą liczby z lili1 oraz lili2, ale pomija liczby podzielne przez X.
lili1=[1,2,3,4,5,6,7,55,9,10]
lili2=[11,12,13,14,15,16]
lilix=[]
x=5


def scal(lili1, lili2, x):
    lili1.extend(lili2)
    for a in lili1:
        if a%x!=0:
            lilix.append(a)
            
scal(lili1,lili2, x)
print(lilix)


