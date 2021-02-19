# write a program create 3*3 matrix using python take all the elements from the user and
#also print the sum of diagonal elements from created matrix
l1 = []
l2 = []
l3 = []
l4 = []
for i in range(0,3):
    l1.append(int(input("enter the fist sublist values")))
for i in range(0,3):
    l2.append(int(input("enter the second sublist values")))
for i in range(0,3):
    l3.append(int(input("enter the third sublist values")))
l4.append(l1)
l4.append(l2)
l4.append(l3)
print(l4)
x= l4[0][0]+l4[1][1]+l4[2][2]
print(x)

