#1.wap covert all the vowels to uppercase for the given input string
def convert_low_to_upp(x):
   v="aeiou"
   output=""
   for i in x:
      if i in v:
         a=chr(ord(i)-32)
         output=output+a
      else:
         output=output+i
   return output
str=input("enter a string:")
res=convert_low_to_upp(str)
print(res)

    
