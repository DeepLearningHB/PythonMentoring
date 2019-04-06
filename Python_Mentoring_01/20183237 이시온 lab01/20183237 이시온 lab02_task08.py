#8

N = "HanbeenOnlineJudge"

B = ""

for i in range(len(N)) :
    if i % 10 == 0 and i !=0 :
       print(B)
       B = ""
    B += N[i]
    i += 1    
print(B)
