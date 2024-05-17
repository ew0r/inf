plik= open('dane.txt','r')
w2= open('w2.txt','w')
x=1
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
                    w2.write(' ')
                    w2.write('2')
                    linia=linia//2
                    w2.write('\n')
                    w2.write(str(linia))
                
                elif linia%3==0:
                    w2.write(' ')
                    w2.write('3')
                    linia=linia//3
                    w2.write('\n')
                    w2.write(str(linia))
                
                elif linia%5==0:
                    w2.write(' ')
                    w2.write('5')
                    linia=linia//5
                    w2.write('\n')
                    w2.write(str(linia))
                
            else:
                w2.write(' ')
                w2.write(str(linia))
                linia=1
                w2.write('\n')
                w2.write(str(linia))
                w2.write('\n')
                break  
w2.close()