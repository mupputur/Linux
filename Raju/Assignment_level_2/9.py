"""
Write a program find a given number is Armstrong or not?  

"""

def arm_strong_or_not(num):      #str=num
    c=0
    for i in num:
        
        c=c+int(i)**len(num)
        

    if str(c)==num:
        return True
    else:
        return False

num=int(input("Enter the number:"))
print(arm_strong_or_not(str(num)))

