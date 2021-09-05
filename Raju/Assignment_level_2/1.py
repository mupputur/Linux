"""
Write a program convert all the vowels to uppercase for the given input string. 

"""

def vowel_upper(input_str):

    output_str=""
    vowels="aeiou"
    
    for ch in input_str:
        if ch in vowels:
            ch=ord(ch)-32
            output_str=output_str+chr(ch)

        else:
            output_str=output_str+ch
    return output_str

input_str=input("Enter a string:")
output_str1=vowel_upper(input_str)
print("output : {}".format(output_str1))
            
