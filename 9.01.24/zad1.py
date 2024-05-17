plik=open('dane.txt','r')
parz=0
nieparz=0

for linia in plik:
    linia=linia.split()
    for elem in linia:
        if int(elem) %2==0:
            parz+=1
        if int(elem) %2==1:
            nieparz+=1
print('Parzyste =',parz)
print('Nieparzyste =',nieparz)

# Policz ile jest liczb parzystych a ile nieparzystych