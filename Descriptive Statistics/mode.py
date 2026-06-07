
number = [1,2,2,2,3,3,3,4,5] 
d ={}
for i in number:
    d[i] = number.count(i)
mode = max(d)
print(d.items())
for mode,value in d.items():

    if value == max(d.values()):
        print("Mode =",mode)