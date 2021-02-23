#13.Write a program find a maximum number in the given input integer list

def max_num(s):
    c=x[0]
    for i in x:
        if c<i:
            c=i
    return c
x=[9,2,3,4,5,6,23]
res=max_num(x)
print(res)
        
