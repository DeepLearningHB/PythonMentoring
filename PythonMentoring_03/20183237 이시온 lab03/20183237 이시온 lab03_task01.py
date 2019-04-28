#1

li = []
re = int(input("정수입력 : "))
li.append(re)

while re != 0 :
    re = int(input("정수입력 : "))
    li.append(re)
print(li)
print(max(li))
print(min(li))
print(sum(li)/len(li))
