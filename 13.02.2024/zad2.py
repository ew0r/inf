x= int(input())
y= list(str(x))


for u in range(1,11):
    a=0
    b=0
    for i in y:
         if a>1 and b==0:
            print(i)
            b+=1
         if i==u:
            a+=1
        
    

