#Utwórz funkcję przemnóż(lili, X). Funkcja zwraca listę z elementami z listy lili przemnożonymi przez X.
lili=[1,2,3,4,5,6,7,55,9,10]
lilix=[]
x=5


def przemnóż(lili, x):
    for a in lili:
        a=a*x
        lilix.append(a)
    return(lilix)    
            
przemnóż(lili, x)    
print(lilix)
