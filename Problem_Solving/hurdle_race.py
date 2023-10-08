parameter = list(map(int, input().split()))

height = list(map(int, input().split()))

height.sort()

max = height[parameter[0]-1]

dose = max-parameter[1] 
if(dose>0):
  print(dose)
else:
  print(0)