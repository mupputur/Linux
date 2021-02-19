x=input("enter even no string ")
if len(x)%2!=0:
    print("invalid input rerun the code")
y=len(x)//2
z=x[y:]+x[:y]
print("last half added with first half of te given string",z)

