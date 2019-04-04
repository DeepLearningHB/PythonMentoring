user = input("그릇이 쌓은 형태를 입력하시오 : ")
length = 10 #length는 그릇의 길이, 첫번째 그릇은 무조건 10으로 시작하므로 10으로 초기화

#while True:      항상 참이므로 무한반복
#     user_count = 0 
#     for i in user:     문자열을 순회하며 user에 있는 "(",")"의 개수 추가
#         if i == "(" or i == ")":
#             user_count += 1
#
#     if user_count == len(user):   user의 길이와 "(",")" 개수가 같으면 while문 탈출
#         break
#        
#     else:
#         user = input("'(' 나 ')' 를 입력해주세요 : ")   다르면 while문으로 돌아감

while user.count("(")+user.count(")") != len(user): #문자열의 총 길이와 "(",")"개수 합이 같을 때 까지 반복
    user = input("'(' 나 ')' 를 입력해주세요 : ")

for i in range(1, len(user)):
    if user[i] == user[i - 1]: #i번째 그릇과 i-1번째의 그릇 모양이 같으면 길이 5 추가 ex) "))"
        length += 5
    else:
        length += 10 #다르면 길이 10 추가 ex) "()"
#Good
print(length)
