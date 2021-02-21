#3.wap to program reverse a given input list

def reverse_list(h):
    output=[]
    for i in range(len(list)-1,-1,-1):
        #print(i)
        output.append(list[i])
    return output
list=[10,20,30,40,50]
res=reverse_list(list)
print(res)

