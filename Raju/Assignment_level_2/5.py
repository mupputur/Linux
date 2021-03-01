
"""
Write a program find a given number is prime or not
"""

def prime_or_not(num):
    c=0
    for i in range(1,num):
        if num%i==0:
            c=c+1
        
    if c>=2:
        return  False
    else:
        return  True    

num=int(input("Enter the number:"))
resp=prime_or_not(num)
print(resp)


        
