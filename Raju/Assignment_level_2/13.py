"""
Write a program find a maximum number in the given input integer list.

"""
def max_num(input_user):
    c=0
    for i in input_user:
        if i>c :
            c=i
    return c
            
input_user=[5,3,10,2,1,4,9]
resp=max_num(input_user)
print(resp)
