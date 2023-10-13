total = int(input())
page = int(input())
least = None

if (total % 2 == 0):
    least = min([page//2, (total-page+1)//2])
else:
    least = min([page//2, (total-page)//2])

print(least)
