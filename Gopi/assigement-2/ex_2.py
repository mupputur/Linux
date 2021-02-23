#2.wap to program reverse a given input string

def reverse_stirng(str):
    output=""
    for ch in str:
        output=ch+output
    return output
str=input("enter a string name:")
res=reverse_stirng(str)
print(res)
