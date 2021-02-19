# write a program create a infinite loop for each loop execution prompt
#the user input if suppose user enters other than integer come out of the loop
#and display all user entered values as list. (use while loop to create infinite loop)
y=[]

"""
while True:
    x= int(input("enter the value"))
    y.append(x)
    if type(x)!=int:
        break
print(y)
"""

while True:
    x= input("enter the integer value or enter char to Quit:")
    if  x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        break
    else:
        x=int(x)
        y.append(x)
print(y)
    
