#3

price={'apple':200, 'banana':300, 'grape':500}
count={'banana':4, 'grape':2, 'apple':3}

for key in price.keys() :
    print(key, price[key],'원',count[key],'개')
