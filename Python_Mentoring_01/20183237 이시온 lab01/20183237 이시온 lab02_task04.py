#4
S = "datastructure"
A = input("알파벳 입력 : ")


B = -1

for i in range(len(S)) :
    if A == S[i] :
        B = i
        break
print(B)
