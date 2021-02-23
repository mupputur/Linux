#14.Write a program print longest length string from given input
#list of strings.


def longest_string(str):
    c=0
    z=""
    for i in str:
        if c<=len(i):
            c=len(i)
            z=i
    return z
str=["java","python","javascirpt","julia","cpp"]
res=longest_string(str)
print(res)
    

