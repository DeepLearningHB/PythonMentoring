sum = 0

user = input("더해줄 마지막 수를 입력하세요 : ")

if(user.isdigit() == True) :
    for i in range(1, int(user) + 1) :
        sum += i

    print(sum)

else :
    print("숫자를 입력해주세요")


