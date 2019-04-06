#2
res = int(input("시험 점수 : "))
#잘못된 입력 시에는 지속적으로 입력을 받아야합니다.

while res > 100 or res < 0 :
   # print(res = int(input("시험 점수 : "))) #변수를 입력받고자 할 때는
    res = int(input("시험 점수 : ")) #와 같은 형태로 입력받아야 합니다.
if res >= 90 :
    print("A")
elif res >= 80 :
    print("B")
elif res >= 70 :
    print("C")
else :
    print("F")

