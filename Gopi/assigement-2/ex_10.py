#10.Write a program that should convert lower case to upper case letter?

def convert_low_to_upp(str):
    output=""
    for ch in str:
        a=chr(ord(ch)-32)
        output=output+a
    return output
str=input("enter a string:")
res=convert_low_to_upp(str)
print(res)


