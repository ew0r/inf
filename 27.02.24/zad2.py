#UŻ podaje liczbę sprawdź czy można utworzyć z niej palindrom poprzez dodanie cyfry na końcu 
r=(input())
e=list(r)
cou=0

for a in range(1,10):
    lst=list(r)
    lst.append(str(a))
    if lst==lst[::-1]:
        cou+=1
         
if cou>0:
    print('TAK')
else:
    print('NIE')

