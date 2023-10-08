n = int(input())
score = list(map(int, input().split()))

inital_max = inital_min = score[0]

min = max = 0

for i in range (1,n):
  if score[i] > inital_max:
    inital_max = score[i]
    max += 1
    
  elif score[i] < inital_min:
    inital_min = score[i]
    min += 1
      
print(max, min)
