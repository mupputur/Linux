#write a program replace each string with an integer value in a given list of strings. the
#replacement integer value should be sum of ascci values of each character of the same string


hr = ["Ganges","Godavari","Brahmaputra","Narmada","Yamuna","Mahanadi","Kaveri","Tapti"]
for i in range(0,len(hr)):
    c = 0
    for j in hr[i]:
        x=ord(j)
        c=c+x
    hr[i] = c
print(hr)
