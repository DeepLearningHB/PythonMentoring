# 3)	세 정수 A, B, C가 주어진다. 이 때 두번째로 큰 정수를 출력하는 프로그램을 작성하시오.
A = 1
B = 13
C = 4
change = 0

a_list = [A, B, C]

# for i in range(3) : range안에 상수를 넣는 습관은 버리는게 좋습니다.
for i in range(3):
    for j in range(2) :
        if a_list[j] > a_list[j+1] :
            change = a_list[i] #이 부분을 a_list[j]로 수정해야합니다.
            a_list[j] = a_list[j+1]
            a_list[j+1] = change
# 위 소스로 할 시
# 1 13 4로 값을 주었을 때 1이 출력이 됩니다.
# 이중 반복문을 안쓰고 하는 방법을 강구해보세요!
print(a_list[1])
