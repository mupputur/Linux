#write a progam to find the no is perfect of not
def perfect_no(n):
    y = 0
    for i in range(1,n):
        if n%i == 0:
            print(i)
            y = y + i
    if n == y:
        return True
    else:
        return False
input_vaue = int(input("enter a value to find the perfect no or not"))
x = perfect_no(28)
print(x)
            
