s=input()
a=[]
for i in s:
    a.append(int(i))
for i in a:
    if a.count(i)!=1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")