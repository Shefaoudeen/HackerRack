n = int(input())
stocks = list(map(int, input().split()))
pairs = 0
visited = []

for i in range (0,n):
  if i not in visited:
    for j in range (i+1,n):
      if stocks[i] == stocks[j]:
        if j not in visited:
          pairs += 1
        visited.append(j)
        break
      
print(pairs)