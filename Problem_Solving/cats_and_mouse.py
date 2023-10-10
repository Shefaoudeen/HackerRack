import math

n = int(input())

for i in range(0, n):
    parameter = list(map(int, input().split()))
    distance1 = abs(parameter[2]-parameter[0])
    distance2 = abs(parameter[2]-parameter[1])

    if (distance1 < distance2):
        print("Cat A")
    elif (distance2 < distance1):
        print("Cat B")
    elif (distance1 == distance2):
        print("Mouse C")
