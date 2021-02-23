#7.Write a program find a factorial of a given number

def factorial(x):
    c=1
    for i in range(1,x):
        c=c+(c*i)
    return ( c)
x=int(input("enter a number:"))
res=factorial(x)
print(res)


