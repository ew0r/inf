plik=open('dane.txt','r')
mcount=0
l1=0
l2=0
l3=0
l4=0
l5=0
l6=0
l7=0
l8=0
l9=0
count=0
for linia in plik:
    if count==0:
        l1+=1
    if count==2:
        l2+=1
    if count==3:
        l3+=1
    if count==4:
        l4+=1
    if count==5:
        l5+=1
    if count==6:
        l6+=1
    if count==7:
        l7+=1
    if count==8:
        l8+=1
    if count==9:
        l9+=1     
    linia=linia.split()
    count=0
    for elem in linia:
        count+=1
        
print('Jednoelementowe =',l1)
print('Dwu =',l2)
print('Trzy =',l3)
print('Cztero =',l4)
print('Pięcio =',l5)
print('Sześcio =',l6)
print('Siedmio =',l7)
print('Ośmio =',l8)
print('Dziewięcioelementowe =',l9)

    


