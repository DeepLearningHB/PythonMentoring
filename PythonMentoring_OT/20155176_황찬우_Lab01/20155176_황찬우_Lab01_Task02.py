sum = 0

user = input("더해줄 마지막 수를 입력하세요 : ")

#if(user.isdigit() == True) :
if user.isdigit(): #다양한 입력 변수에 대한 처리 Good / user.isdigit() 만 써도 됩니다!
    for i in range(1, int(user) + 1) :
        sum += i
    print(sum)

else :
    print("숫자를 입력해주세요")


