x = input("entere the first element grater than five charecter  :")
if len(x)<=5:
    print("invalid input rerun code")
y = input("enter the secon element grather than five charecters  :")
if len(y)<=5:
    print("invalid input rerun code")
z = x[len(x)-3:]+y[:3]
print("the cobination of the two strings",z)
