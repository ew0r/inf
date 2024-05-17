i='1236 4567 8999 33 3 4'
lista=i.split()
temp=[]
l1=0
l2=0
l3=0
l4=0
for elem in lista:
    for liczba in elem:
        temp.append(liczba)
        
    ilec=len(temp)
    if ilec==1:
        l1+=1
    if ilec==2:
        l2+=1
    if ilec==3:
        l3+=1
    if ilec==4:
        l4+=1
    temp=[]    
print(l1)
print(l2)
print(l3)
print(l4)