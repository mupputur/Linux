x = input("enter a string more than five charecters  :")
count=""
for i in range(len(x)):
    count= count+x[i]+'-'
y=count[:len(count)-1]
print(y)
