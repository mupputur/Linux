"""
Write a program construct two dimensional array and print the same.

"""     
def two_dimensional():
    
    m=[]
    for i in range(0,3):
        n=[]
        for j in range(0,2):
            input_user=int(input("Enter the number:"))
            
            n=n+[input_user]
        m=m+[n]
    return m
    
resp=two_dimensional()
print(resp)

