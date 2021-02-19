# write a program find all the even number form the give list


lis = [18.8,"hyd",18,26.9,19,"bang",26,33.7,25,"chen"]
li=[]
for i in range(len(lis)):
    if type(lis[i])==int:
        if lis[i]%2==0:
            li.append(lis[i])
print("list of the even number form the given list",li)
            
