#2
res = int(input("시험 점수 : "))

if res > 100 or res < 0 :
    print(res = int(input("시험 점수 : ")))
elif res >= 90 :
    print("A")
elif res >= 80 :
    print("B")
elif res >= 70 :
    print("C")
else :
    print("F")

