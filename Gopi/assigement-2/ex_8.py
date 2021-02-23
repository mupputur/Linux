#8.wap a program count number of occurance of vowels in a given stirng

def count_num_occurance_vowels(str):
    d={}
    v= "aeiou"
    for ch in str:
        if ch in v:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]=d[ch]+1
    return d

str=input("enter a string:")
res=count_num_occurance_vowels(str)
print(res)
