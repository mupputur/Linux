#5.wap a program to find gievn number is prime or not
def num_prime_or_not(x):
    if x>0:
        for i in range(2,x):
            #print(i)
            if x%i == 0:
                v= "{} is not prime number".format(x)
                break
            else:
                v ="{} is a prime number".format(x)
    else:
        v= "{} is not prime numbr".format(x)
    return v

num=int(input("enter a number:"))
res=num_prime_or_not(num)
print(res)


