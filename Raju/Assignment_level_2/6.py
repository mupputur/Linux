"""
Write a program find given number is perfect or not
"""

def perfect_or_not(num):
    output_num=0
    
    for i in range(1,num):
    
        if num%i==0:
            output_num=output_num+i

    if num==output_num:
        return True
    else:
        return False

num=int(input("Enter the number:"))   
resp=perfect_or_not(num)
print(resp)
