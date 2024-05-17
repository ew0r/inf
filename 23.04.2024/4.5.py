plik=open('txt.txt', 'r')
konta=[]
obkonta=[]
fake=[]
finalobkonta=[]
betkonta=[]
poprzednielem=''
a=1
b=1
for linia in plik:
    for elem in linia.split():
        if elem not in konta:
            konta.append(elem)

        if a%2==0:
            obkonta.append(elem)
        a+=1

for elem in konta:
    if elem not in obkonta:
        fake.append(elem)
        
print('2')
for linia2 in plik:
    print('1')
    for elem in linia2.split():
        print('1')
        if a%2==0 and poprzednielem not in fake:
            finalobkonta.append(elem)
        b+=1
        poprzednielem=''
        poprzednielem=elem

for konto in konta:
    konto=str(finalobkonta.count(konto))+' '+konto
    betkonta.append(konto)
betkonta.sort()
print(betkonta[-1])