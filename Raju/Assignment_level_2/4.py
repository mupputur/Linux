"""
Write a program print the  Fibonacci series  till 100

"""

def fibnoic_series(input_user):
    x=[0,1]
    
    while True:
        next_num=x[-1]+x[-2]
      
        if next_num > input_user:
            break
        x.append(next_num)
    return x

input_user=int(input("Enter the number:"))
resp=fibnoic_series(input_user)
print(resp)


