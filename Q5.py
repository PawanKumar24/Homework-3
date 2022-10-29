# Pawan Kumar
# ID: 2046222
outputArr= []
values = input().split()
values = [int(val) for val in values]
for val in values:
    if val >= 0:
        outputArr.append(val)
        pass
outputArr.sort()
for i in range(len(outputArr)):
    if i == len(outputArr)-1:
        print(f'{outputArr[i]}',end =" ")
    else:
        print(f'{outputArr[i]} ',end='')

