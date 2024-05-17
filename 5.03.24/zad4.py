#Utwórz funkcję wielokrotnie(lili). Każdy element z listy wypisz tyle razy ile wynosi jego wartość.

lili=[1,2,3,4,5,6,7,8,9,10]
x=5

def wielokrotnie(lili):
    for a in lili:
        b=int(a)
        while b>0:
            print(a)
            b-=1
            
wielokrotnie(lili)    
