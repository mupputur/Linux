
#15.Write a program count duplicated elements in the list

def count_duplicate_element(x):
    a={}
    count=0
    for ele in x:
        if ele not in a:
             a[ele]=1
        else:
            a[ele]=a[ele]+1
            
    return a
            
x=[401,403,409,403,453,402,438,401,444]
res=count_duplicate_element(x)
print(res)

