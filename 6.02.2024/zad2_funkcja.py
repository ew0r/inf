plik= open('dane.txt','r')
w2= open('w2.txt','w')
x=1
def spacje(p,lin):
    global linia
    linia=lin//int(p)
    w2.write(' ')
    w2.write(p)
    w2.write('\n')
    w2.write(str(linia))
    return
                                    
for linia in plik:
    linia=int(linia)
    if x!=1:
        w2.write('\n')
    w2.write(str(linia))
    x-=1
    while linia>1:
        for i in range(2,linia):
            if (linia % i) == 0:
                if linia%2==0:
                    spacje('2',linia)
                elif linia%3==0:
                    spacje('3',linia)
                elif linia%5==0:
                    spacje('5',linia)
            else:
                w2.write(' ')
                w2.write(str(linia))
                linia=1
                w2.write('\n')
                w2.write(str(linia))
                w2.write('\n')
                break  
w2.close()    