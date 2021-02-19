#write a program reverse each string from the given list and finally reverse a list
x = ["odd","even","sum"]
print("the existing list ",x)
for i in range(len(x)):
    x[i]=x[i][::-1]
x.reverse()
print("the reversed list of string",x)
