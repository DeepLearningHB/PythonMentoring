new_dic = dict() #새로운 딕셔너리 만들기

for key in dic.keys(): 
    re = [] #새로운 리스트 만들기
    a = dic[key][:]
    a.insert(0, a[-1]) #1월 앞에 12월 만들기
    a.append(a[1]) #12월 뒤에 1월 만들기
    
    for i in range(1, len(a)-1): #1월부터 12월 구간 돌기
        if a[i] > a[i-1] and a[i] > a[i+1]: # a[i]가 앞 숫자와 뒷 숫자보다 크면 새롭게 만든 리스트에 추가하기
            re.append(i)
    
    new_dic[key] = re #리스트를 딕셔너리에 옮기기
    
print(new_dic)
