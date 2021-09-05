"""
Write a program reverse the given input list
"""

def reverse_list(input_list):
    output=[]
    for items in input_list:
        output=[items]+output
    return output

input_list=[1,2,3,4,5,6,7,8]  
resp=reverse_list(input_list)
print(resp)
