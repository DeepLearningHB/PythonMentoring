N = "Pneumonoultramicroscopicsilicovolcanoconiosis"

count = 0
str = ''

for i in N:
    
    if count % 10 == 0 and count != 0:
        print(str)
        str = ''
        
    str += i    
    count += 1
print(str)
