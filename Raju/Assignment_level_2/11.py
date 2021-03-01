"""
Write a program sort the given list of integer elements

"""


def sort_list(input_list):

    for i in range(len(input_list)):
        for j in range(1,len(input_list)):
            if input_list[i]<input_list[j-1]:
                input_list[i],input_list[j-1]=input_list[j-1],input_list[i]
    return input_list
            
    
input_list=[123,124,126,125,129,127,120,121,122,128]
resp=sort_list(input_list)
print(resp)
