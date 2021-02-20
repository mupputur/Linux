# write a program to find the factorial of the given value
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
input_value = int(input("enter the value to find the factorial"))
x = factorial(5)
print(x)    
