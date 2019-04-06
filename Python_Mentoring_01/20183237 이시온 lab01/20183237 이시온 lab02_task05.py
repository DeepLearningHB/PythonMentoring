#5
S = input("문자열 입력 : ")
A = input("알파벳 입력 : ")

count = 0

for i in range(len(S)) :
    if A == S[i] :
        count +=1
print(count)
