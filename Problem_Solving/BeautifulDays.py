def reverse(number):
    reverse_num = 0
    while number != 0:
        digit = number % 10
        reverse_num = reverse_num*10 + digit
        number //= 10
    return reverse_num


parameter = list(map(int, input().split()))
count = 0

for i in range(parameter[0], parameter[1]+1):
    reverse_num = reverse(i)
    difference = i-reverse_num
    difference /= parameter[2]

    new = int(difference)
    if (new == difference):
        count += 1

print(count)
