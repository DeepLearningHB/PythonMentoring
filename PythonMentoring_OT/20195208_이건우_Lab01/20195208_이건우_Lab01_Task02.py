num = int(input("더할 숫자를 입력하세요: "))

i = 1
add = 0

while i <= num:
    add += i
    i += 1
#for와 while문은 동일한 기능을 하지만, 실제 사용시는 상황에 따라 다르게 사용합니다.
# 멘토링 시간에 알려드릴게요.
print(add)
