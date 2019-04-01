region_list = ["서울", "대전", "대구", "부산", "울산", "인천"]

# 반복이 0~4까지만 돌 것 같습니다. range(6) 보단 리스트의 길이가 일정하지 않을 때에는 range(len(region_list)) 권장합니다.
# 실제 프로그램에서는 길이가 일정하지 않는 경우가 매우 많아요.
for i in range(5):  

    print("나는", region_list[i], "사는 사람입니다.")
#권장 코드
'''
for i in region_list:
    print("나는", i, "사는 사람입니다.")
'''
