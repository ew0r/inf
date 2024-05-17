plik=open('n_z.txt','r')
mcount=0

for linia in plik:
    linia=linia.strip()
    for elem in linia:
        if elem != ' ':
            mcount+=int(elem)
print(mcount)        
        