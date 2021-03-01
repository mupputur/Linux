"""
Write a program that should convert lower case to upper case letter?
"""
def lower_to_upper(input_str):

    output_str=""
    for ch in input_str:
        if 97<=ord(ch)<=122:
            ch=ord(ch)-32
            output_str=output_str+chr(ch)

        else:
            output_str=output_str+ch

    return output_str

            
input_str=input("Enter the number:")

resp=lower_to_upper(input_str)

print(resp)
