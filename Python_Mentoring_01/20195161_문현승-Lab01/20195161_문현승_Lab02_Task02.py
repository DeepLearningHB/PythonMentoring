test=int(input("test: "))
while test<0 or test>100:
    test=int(input("test: "))
if test<=100 and test>=90: print("A")
elif test>=80: print("B")
elif test>=70: print("C")
else: print("F")