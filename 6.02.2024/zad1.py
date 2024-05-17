plik= open('dane.txt','r')
prime= open('prime.txt','w')
odd=open('odd.txt','w')

for linia in plik:
    linia=int(linia)
    
    if linia>1:
        for i in range(2,linia):
            if (linia % i) == 0:
                print(linia, file=odd)
                break
            else:
                print(linia, file=prime)
                break
prime.close()
odd.close()