#4.Write a program print the Fibonacci series  till 100

def fiboncci_series(num):
    x=[0,1]
    while True:
        y=x[-1]+x[-2]
        if y>num:
            break
        x.append(y)
    return x
num=int(input("enter a number:"))
res=fiboncci_series(num)
print(res)
        
