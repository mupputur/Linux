#11.wap sort the given list of interger elements
#"""
def sort(x):
    for i in range(len(x)):
        #print(i)
        for j in range(1,len(x)):
            #print(j)
            if x[i]<x[j-1]:
                x[i],x[j-1]=x[j-1],x[i]
    return x
x=[5,3,4,2,3,2,1,-2,-1]
res=sort(x)
print(res)
#"""
        
