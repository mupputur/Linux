"""

Write a program reverse a given input string
"""

def reverse_str(input_str):
    
    output_str=""
    for ch in input_str:
        output_str=ch+output_str
    return output_str

input_str=input("Enter a string:")
resp=reverse_str(input_str)
print(resp)

        
