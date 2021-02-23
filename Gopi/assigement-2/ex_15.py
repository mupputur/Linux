#15.Write a program count duplicated elements in the list

def count_duplicate_element(x):
    a=[]
    d=[]
    for ele in input_list:
        if ele not in a:
            a.append(ele)
        else:
            d.append(ele)
    return d
input_list=[401,403,409,403,453,402,438,401,444]
res=count_duplicate_element(input_list)
print(res)

