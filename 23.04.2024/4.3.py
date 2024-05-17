plik=open('txt.txt', 'r')
rpary=[]
wait=[]
kwait=[]
pary=[]
a=0
count=0
for linia in plik:
    if a!=0:
        rpary.append(wait)
        pary.append(kwait)
        wait=[]
        kwait=[]
    for elem in linia.split():
        wait.append(elem)
        wait.reverse()
        kwait.append(elem)
        a+=1
               
#rpary[-1]=linia+'\ #stringi można normalnie dodawać ha
#pary[-1]=linia+'\n'
for elem in rpary:
    if elem in pary:
        count+=1
print(count//2)