num =int(input()) #숫자입력
for i in range(1,num+1):
    print(" "*(num-i)+ "*"*(2*i-1)) #1부터 num+1까지 앞부분 공백두고 2i-1 기준으로 별 출력
for j in range(num-1,0,-1): #num-1~0 까지 앞부분 공백두고 2j-1 기준으로 별 출력
    print(" "*(num-j)+"*"*(2*j-1))
    