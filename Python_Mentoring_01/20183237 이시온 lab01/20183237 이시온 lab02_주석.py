user = input("그릇이 쌓은 형태를 입력하시오 : ") #그릇의 형태 입력 받는다.
length = 10 # length의 초기 값은 10이다.

# while True: #참일 때 반복
#     user_count = 0 #user_count의 초기 값은 0이다.
#     for i in user: #user에 입력 받은 그릇의 형태 문자열 차례로 반복한다.
#         if i == "(" or i == ")": 
#             user_count += 1 #"(" 이나 ")"의 형태일 때 user_count에 1을 더한다.
#
#     if user_count == len(user):
#         break #user_count의 값이 입력 받은 user의 길이와 같다면 멈춘다.
#
#     else:
#         user = input("'(' 나 ')' 를 입력해주세요 : ") #"(" 이나 ")"가 아닌 다른 것을 입력했을 때 다시 입력하도록 유도한다.

while user.count("(")+user.count(")") != len(user): #"(" 와 ")"를 더한 값이 user에 입력한 값과 같을 때까지 반복한다.
    user = input("'(' 나 ')' 를 입력해주세요 : ")

for i in range(1, len(user)):
    if user[i] == user[i - 1]:
        length += 5 #i의 그릇 형태와 i-1의 그릇 형태가 같다면 length에 5를 더한다.
    else: #다르다면 10을 더한다.
        length += 10
print(length) #그릇의 총 길이 length를 출력한다.
