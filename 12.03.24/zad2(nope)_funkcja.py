#policz średni wiek (licząc lata)
plik=open("ludzie.txt", 'r', encoding='utf-8')
m=0
k=0
mr=0
kr=0

def morw(linia,m,mr,w,wr):


for linia in plik:
    linia=linia.split()
    
    if linia[4]== 'M':
        m+=1
        data=list(linia[3])
        rok=data[-4:]
        s=[str(i) for i in rok]      #jojnk
        rok=int(("".join(s)))        #jojnk
        mr+=2024-rok
        
        
print('Średni wiek kobiet =',mr//m)
print('Średni wiek mężczyzn =',kr//k)
