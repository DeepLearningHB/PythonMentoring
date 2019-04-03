
user = input("그릇이 쌓은 형태를 입력하시오 : ")
length = 10

# while True:
#     user_count = 0
#     for i in user:
#         if i == "(" or i == ")":
#             user_count += 1
#
#     if user_count == len(user):
#         break
#
#     else:
#         user = input("'(' 나 ')' 를 입력해주세요 : ")

while user.count("(")+user.count(")") != len(user): #내장함수를 활용하세요!
    user = input("'(' 나 ')' 를 입력해주세요 : ")

for i in range(1, len(user)):
    if user[i] == user[i - 1]:
        length += 5
    else:
        length += 10
#Good
print(length)
# 추가 피드백: 아무것도 입력하지 않았을 시 10이 출력됨, 예외 처리가 필요해보임. 
