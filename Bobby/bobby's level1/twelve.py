x = int(input("the length of the list"))
y=[]
z=[]
for i in range(x):
    y.append(int(input("enter the number type values   :")))
    if y[i]%2==0:
        z.append(y[i])
print("even number in the given list",z)
        
    
