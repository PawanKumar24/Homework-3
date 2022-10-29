
# Pawan Kumar
# ID: 2046222
temp = {}
arr = input().split()
for value in arr:
   if value in temp:
      temp[value] += 1
   else:
      temp[value] = 1
for value in arr:
   print(f'{value} {temp[value]}')
