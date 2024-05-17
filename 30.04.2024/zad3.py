i='123 456 992'
lista=i.split()
parzyste=0
nieparzyste=0
for elem in lista:
    if int(elem)%2==0:
        parzyste+=int(elem)
    else:
        nieparzyste+=int(elem)

print(parzyste)
print(nieparzyste)
