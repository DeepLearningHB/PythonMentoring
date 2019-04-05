s=input("s: ")
str=""
for i in range(len(s)):
    if i%10==0 and i!=0:
        print(str)
        str=""
    str += s[i]
    i +=1 
print(str)