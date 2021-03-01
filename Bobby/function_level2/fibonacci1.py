# write a program print the fibonacci series till 100
def fibonacci(input_value):
   x = [0,1]
   while True:
      value = x[-1]+x[-2]
      if value > input_value:
         break
      x.append(value)
   return x
y = fibonacci(100)
print(y)
         
