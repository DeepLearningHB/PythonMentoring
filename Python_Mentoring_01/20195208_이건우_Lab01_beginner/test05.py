S = input("문자열 입력: ")

A = input("알파벳 입력: ")
count = 0
for i in S:
    if A == i:
        count += 1
        
if count != 0:
    print(count)
else:
    print(-1)
