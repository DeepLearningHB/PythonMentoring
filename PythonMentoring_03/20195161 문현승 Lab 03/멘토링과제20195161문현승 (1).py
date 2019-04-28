1번문제

a=int(input())
 		#정수입력
list=[] 			#빈 리스트생성
sum=0 			#sum은 0
while a>0 or a<0 :
		#a가 0이 아니면 계속 하는 반복문
  a=int(input())
		#정수입력
  list.append(a)
		#리스트에 a추가
max=list[0]		#max는 리스트에 0자리 숫자
min=list[0]
		#min은 리스트에 0자리 숫자
for i in list:
		#i를 list만큼 반복
  sum=sum+i
		#sum은 sum+i
  if i>=max:		#i가 맥스보다 크면
    max=i
			#맥스는 i
  elif i<=min:		#i가 민보다 작으면
    min=i			#민은 i
eve=sum/len(list)		#eve는 sum 나누기 리스트 길이
print(list,max,min,eve)	#리스트랑 맥스랑 민이랑 eve 출력

2번문제

dic={1:"one",2:"two",3:"three"}	#키1 벨루 one 키2 벨루two 키3 벨루three 딕셔너리 생성
print(len(dic))			#딕셜너리 길이 출력
print(list(dic.keys()))		#딕셔너리 키 출력
print(list(dic.values()))		#딕셔너리 벨루 출력
for key, value in dic.items():		#키변수와 벨루변수를 딕셔너리 아이템만큼 반복하는 빈복문
  print(key,value)			#key와 벨루출력

3번문제

price={'apple':200,'banana':300,'grape':500}	#키apple 벨루200 키banana 벨루300 키grape 벨루500인 프라이스 딕셔너리 만듦
count={'apple':3,'banana':4,'grape':2}		#키apple 벨루3 키banana 벨루4 키grape 벨루2인 카운트 딕셔너리 만듦
sum=0					#sum은 0
for key in price.keys():			#키변수를 프라이스의 키만큼 반복하는 반복문
  sum+=price[key]*count[key]		#sum은 프라이스키 곱하기 카운트키에 sum을 더한 값
  print(key,price[key],count[key])		#key와 프라이스키, 카운트키를 출력
print(sum)				#sum 출력

5번문제
dic= { ‘adidas’: [0, 10, 20, 30, 20, 10, 20, 2, 10, 8, 11, 15],		#키adidas 벨루[0, 10, 20, 30, 20, 10, 20, 2, 10, 8, 11, 15]
 ‘descente’: [11, 12, 11, 10, 8, 9, 15, 13, 10, 10, 10, 10],		#키descente 벨루[11, 12, 11, 10, 8, 9, 15, 13, 10, 10, 10, 10]	
 ‘nike’: [0, 11, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],			#키nike 벨루[0, 11, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
‘fila’: [10, 10, 15, 20, 30, 40, 20, 30, 10, 11, 12, 13] }		#키fila 벨루[10, 10, 15, 20, 30, 40, 20, 30, 10, 11, 12, 13]인 딕셔너리 생성

﻿new_dic = dict() 						#뉴딕이라는 이름의 빈 딕셔너리 생성

 for key in dic.keys():					#키변수를 딕의 키만큼 반복하는 반복문
     re = []						#리라는 이름의 빈 리스트
     a = dic[key][:]						#a는 딕의 키를 복사한 딕셔너리
     a.insert(0, a[-1])					#a딕셔너리 0의 자리에 a[-1]의 수를 추가
     a.append(a[1])						#a딕셔너리에 a[1]을 추가
     for i in range(1, len(a)-1):				#i변수를 1부터 시작 a의 길이에서 1을 뺀 만큼 반복하는 반복문
         if a[i] > a[i-1] and a[i] > a[i+1]:				#if a[i]가 a[i-1]보다 크고 a[i]가 a[i+1]보다 크면	
             re.append(i)					#리리스트에 i추가
     new_dic[key] = re					#뉴딕의 키는 리
 print(new_dic) 						#뉴딕출력
