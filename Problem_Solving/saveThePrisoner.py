n = int(input())

for i in range(0, n):
    data = list(map(int, input().split()))
    start = data[2]
    total = data[0]
    while data[1] != 1:
        if start != total:
            start += 1
            data[1] -= 1
        else:
            start = 1
            data[1] -= 1
    print(start)
