i='123 456 992 23 25 98'
lista=i.split()
count=0

for elem in lista:
    if int(elem)>100:
        count+=1
print(count)        