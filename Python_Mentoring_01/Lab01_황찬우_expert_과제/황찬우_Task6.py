user = int(input("최대치를 입력하시오 : "))
list = [1, 1]
i = 2

while True:

    list.append(list[i - 2] + list[i - 1])  # 계산하여서 list에 추가함

    if list[i] > user:  # 처음으로 user값을 넘을시 break
        break

    i += 1

print("처음으로 %d 를 넘은 인덱스는 : %d" % (user, i+1)) #입력 값 15일때 출력은 8이 되어야 합니다. i+1로 수정
# 1 1 2 3 5 8 13 21

#과제 총평
#전체적으로 훌륭히 잘 수행하였음 .
#문제를 조금 꼼꼼히 읽어서 제시된 조건에 맞출 필요가 있음.