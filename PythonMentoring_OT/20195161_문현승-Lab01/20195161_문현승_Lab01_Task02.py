#과제는 1부터 더하는 내용이였습니다.
#사소할 수 있지만 문제의 요구조건에 맞춰주는게 좋아요!
a=int(input())
sum=0
for i in range(1, a+1): # range의 자동 incease는 1입니다. 생략해도 됩니다. 
    sum+=i # += 연산자가 있다는 것을 기억해주세요!
print(sum)
