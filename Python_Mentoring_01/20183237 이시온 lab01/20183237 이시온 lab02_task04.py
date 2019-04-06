#4
S = "datastructure"
A = input("알파벳 입력 : ")


B = -1 #목적이 있는 변수 명은 적당히 알맞게 지어줘야 좋습니다. index = -1

for i in range(len(S)) :
    if A == S[i] :
        B = i
        break
print(B)
