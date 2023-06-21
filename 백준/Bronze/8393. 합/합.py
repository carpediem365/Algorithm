sum =0
num = int(input())
while True:
    sum += num
    num -= 1
    if num == 0:
        break
print(sum)