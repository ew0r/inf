plik=open('txt.txt', 'r')
konta=[]
obkonta=[]
betkonta=[]
a=1
for linia in plik:
    for elem in linia.split():
        if elem not in konta:
            konta.append(elem)

        if a%2==0:
            obkonta.append(elem)
        a+=1

for konto in konta:
    konto=str(obkonta.count(konto))+' '+konto
    betkonta.append(konto)
betkonta.sort()
print(betkonta[-1])