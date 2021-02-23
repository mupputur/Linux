#6.Write a program find given number is perfect or not

def per_or_not(x):
    y=0
    for i in range(1,x):
        print(i)
        if x%i==0:
            y=y+i
    if x==y:
        return "perfect number"
    else:
        return "not perfect number"
        
num=int(input("enter a number:"))
res=per_or_not(num)
print(res)

    
