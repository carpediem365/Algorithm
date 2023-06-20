N,M=map(int,input().split())
if 1<=N<=100 and 1<=M<=10000:
    if M <= N*100:
        print("Yes")
    else:
        print("No")
else:
    print("범위초과")
