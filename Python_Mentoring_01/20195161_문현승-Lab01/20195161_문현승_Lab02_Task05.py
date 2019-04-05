s=input("s: ")
a=input("a: ")
count=0
for i in range(len(s)):
    if a==s[i]:
        count+=1
if count>0: print(count)
else: print("-1")