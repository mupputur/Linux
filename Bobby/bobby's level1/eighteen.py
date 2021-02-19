#write a program create a random list of length
#10 print all the elements exvept the elements which are divisible by 4
y=[]
x=[]
for i in range(10):
    y.append(int(input("enter the value :")))
    if y[i]%4!=0:
        x.append(y[i])
print("the values that are not divided by four  ",x)
    
