#두팀이 득점한 점수합과 차
# a+b =4
# a-b = 2
# 2a =4 a=2 b=1
A,B = map(int,input().split())
 #A+B =4, C=2a
A_SCORE = int((A+B)/2)
B_SCORE = int((A-B)/2)
if (A+B)%2 ==0 and (A>=B):
    print(A_SCORE,B_SCORE)
else:
    print(-1)
