plik=open('txt.txt', 'r')
konta=[]
for linia in plik:
    for elem in linia.split():
        if elem not in konta:
            konta.append(elem)

print(len(konta))        