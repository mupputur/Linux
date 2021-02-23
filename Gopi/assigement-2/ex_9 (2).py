#9.Write a program find a given number is Armstrong or not?

def Armstrong_or_not(x):
    c=0
    for i in x:
        c=c+int(i)**len(x)
    print( c)
    
    if str(c)==x:
        return True
    else:
        return False
    
x=int(input("enter a number:"))
res=Armstrong_or_not(str(x))
print(res)

    
