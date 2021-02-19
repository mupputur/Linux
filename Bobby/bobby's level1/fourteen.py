x = int(input("enter the length of the string  :"))
y = []
for i in range(x):
    y.append(input("enter the string based on the length   :"))
    y[i]=len(y[i])*y[i]
print(y)
