"""
Write a program find a factorial of a given number
"""


def find_factorial(num):

    for i in range(num-1 ,-1 ,-1):
        if i>0: #54321
            num=num*i
    return num
            
    
num=int(input("Enter the number:"))
resp=find_factorial(num)
print(resp)

          
