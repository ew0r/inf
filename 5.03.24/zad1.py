#Utwórz listę zawierającą liczby z przedziału A, B, podzielne przez X
a=int(input())
b=int(input())
x=int(input())
cyfr=[]
for y in range(a,b+1):
    if y%x==0:
        cyfr.append(y)
        