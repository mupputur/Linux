"""
Write a program count duplicated elements in the list

"""

def count_duplicate_elem(input_list):

    output={}
    for elements in input_list:
        if elements not in output:
            output[elements]=0
        else:
            output[elements]=output[elements]+1

    return output

input_list=[10,20,30,40,40,20,50,50,60,10,20,10]
resp=count_duplicate_elem(input_list)
print(resp)
