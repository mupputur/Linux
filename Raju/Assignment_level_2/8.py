"""
Write a program count number of occurrences of vowels in a given string. 

"""

def count_vowels(input_str):
    v={}
    vowels="aeiou"

    for ch in input_str:
        if ch in vowels:
            if ch not in v:
                v[ch]=1
            else:
                v[ch]=v[ch]+1
                
    return v

            
input_str=input("Enter the string:")
resp=count_vowels(input_str)
print(resp)
    
