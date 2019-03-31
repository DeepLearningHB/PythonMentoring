user = int(input("더해주는 마지막 수를 입력하시오 : "))

if (user%2) != 0 :
    print((1 + user) * (user//2) + user//2)

else :
    print((1 + user) * (user//2))

sum = 0
for i in range(1, 100):
    sum+=i
print(sum)