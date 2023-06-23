num1 = int(input())
num2 = list(map(int, input()))
num3=0
num4=0
num5=0
total=0
for i in range(2,-1,-1):
        if i ==2:
            num3 += num1 * num2[i]
        elif i == 1:
            num4 += num1 * num2[i]
        elif i == 0:
            num5 += num1 * num2[i]
total = num3+(num4*10)+(num5*100)
print(num3)
print(num4)
print(num5)
print(total)