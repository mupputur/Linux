#write a program convert the following list to a dictionary



x = [("A",65),("B",66),("C",67),("D",68)]
d={}
for i in x:
    d[i[0]]=i[1]
print("convert the following list to a dictionary ",d)
