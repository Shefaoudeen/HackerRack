parameter = list(map(int, input().split()))

price = list(map(int, input().split()))

charged = int(input())
total = 0

for i in range (0,parameter[0]):
  if i != parameter[1]:
    total += price[i]

total = int(total/2)

if(total == charged):
  print('Bon Appetit')
  
else:
  print(charged-total)