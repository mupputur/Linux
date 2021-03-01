"""
Write a program print longest length string from given input list of strings. 

"""


def longest_str(input_str):
    
    c=0
    z=""
    for i in input_str:
        if c<=len(i):
            c=len(i)
            z=i
            
    return z

input_str=['raju','rakesh','siri','rajkumar']

resp=longest_str(input_str)
print(resp)
