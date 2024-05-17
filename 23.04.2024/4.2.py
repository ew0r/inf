plik=open('txt.txt', 'r')
konta=[]
obkonta=[]
fake=[]
a=1
for linia in plik:
    for elem in linia.split():
        if elem not in konta:
            konta.append(elem)

        if a%2==0:
            if elem not in obkonta:
                obkonta.append(elem)
        a+=1

for elem in konta:
    if elem not in obkonta:
        fake.append(elem)

print(fake)