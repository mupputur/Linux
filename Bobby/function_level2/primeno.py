# write a program to find whether the given no is prime or not
def prime_number(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count = count + 1
    if count ==2:
        return True
    else:
        return False
input_value = int(input("enter the value to find the enterd value is prime are not"))
x = prime_number(input_value)
print(x)
