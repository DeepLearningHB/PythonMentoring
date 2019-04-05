s="datastructure"
a=input(" ")
index=-1
for i in range(len(s)):
    if a==s[i]:
        index=i
        break
print(index)