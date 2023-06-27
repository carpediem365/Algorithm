# 자연수 p,q가 있을때 p/q 나머지 0이면 q는 p의 약수
# N의 약수들중 k번쨰로 작은수 출력 
num = list(map(int,input().split())) #n,k 입력받아 리스트에 저장
num1=num[0] #n의 약수를 구하기 위해 사용
measure_list=[] #약수 리스트
for i in range(1,num1+1): #1~자연수num1+1까지 
    if num1 % i ==0: #나머지가 0이면 i는 num1의 약수
        measure_list.append(i) #약수리스트에 i 추가
if len(measure_list) >num[1]-1: #약수의 개수가 k보다 클경우
    print(measure_list[num[1]-1]) #약수리스트에서 k번째 작은수 출력
else:
    print(0) #n의 약수의 개수가 k보다 적을경우 0출력 
    
    