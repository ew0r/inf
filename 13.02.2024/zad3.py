x=int(input())
y=str(x)
dwucyfry=[]
trzycyfry=[]

for a in y:
    if int(a)%2==0:
        dwucyfry.append(a)
        dwucyfry.sort(reverse=True)
    if int(a)%2==1:
        trzycyfry.append(a)
        trzycyfry.sort(reverse=True)

print("Max wartość z parzystych:",''.join(dwucyfry))
print("Max wartość z nieparzystych:",''.join(trzycyfry))