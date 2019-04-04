S = "datastructure"

A = input("알파벳 입력: ")
index = 0

for i in S:
    if A == i:
        print(index)
        break
    else:
        index += 1
