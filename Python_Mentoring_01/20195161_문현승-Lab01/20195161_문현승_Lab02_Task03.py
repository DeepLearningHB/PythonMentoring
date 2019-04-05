a=[10, 4, 2, 7, 6, 1, 5, 8]
max=a[0]
min=a[0]
for i in a:
    if i>=max: max=i
    elif i<=min: min=i
print(max, min)