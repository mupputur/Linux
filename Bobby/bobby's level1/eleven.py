x = int(input("entere the length of the list "))
y=[]
z=[]
for i in range(x):
    y.append(input("enter the strings"))
    if len(y[i])%2 !=0:
        z.append(y[i])
print("odd length strings",z)
        
    
