money = int(input())
n = int(input())
receipt = 0
for i in range(n):
    a,b = map(int,input().split())
    receipt+=(a*b)
    
if money == receipt:
    print('Yes')
else:
    print('No')
