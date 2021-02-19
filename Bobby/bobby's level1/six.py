# write a program print all duplicated values in desvending order form the given input list
il = [401,403,409,403,453,402,438,401,444]
dupe = []
x = len(il)
for i in range(x):
    k = i+1
    for j in range(k,x):
        if il[i] == il[j] and il[i] not in dupe:
            dupe.append(il[i])
dupe.sort(reverse=True)
print(dupe)

    
