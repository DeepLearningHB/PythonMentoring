score = int(input("점수 입력: "))

if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=70:
    grade = 'C'
else:
    grade = 'F'

print(grade)
