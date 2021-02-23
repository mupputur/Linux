#12.Write a program construct two dimensional array and print the same
#"""
def two_dimensional():
    l=[]
    for i in range(0,3):
        m=[]
        for i in range(0,2):
            x=int(input("enter a number:"))
            m=m+[x]
        l=l+[m]
    return l
#x=int(input("enter a number:"))
res=two_dimensional()
print(res)
#"""
