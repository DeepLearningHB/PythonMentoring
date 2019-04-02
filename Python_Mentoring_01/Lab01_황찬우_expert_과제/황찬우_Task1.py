# 2)	정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 입력) 길이가 N인 수열 A를 생성하고 비교할 정수 X를 초기화한다.
# 출력) 수열 A에서 X보다 작은 수를 모두 출력한다.

A_list = []
N = 10
X = 6

for i in range(N) :
    A_list.append(i+1)

for i in range(len(A_list)) :
    if A_list[i] < X :
        print(A_list[i], end = " ")
# Good
