## 완전수란 n이 자신을 제외한 모든 약수들의 합과 같은것
#n의 약수를 구하고 자기자신을 제외한 합을더해서 비교
#약수들은 오름차순으로 냐열
#완전수가 아니라면 n is NOT perfet.

measure_list =[]
result =""
while True: #-1 나오기 전까지 계속 반복
    num = int(input())
    if num ==-1:#-1이나 나오면 break
        break
    for i in range(1,num): #1~num-1까지 num%i ==0인 i를 약수리스트에 저장
        if num%i ==0:
            measure_list.append(i)
    if num == sum(measure_list): #완전수인지 판단
        for i in measure_list:#약수리스트에 값을 하나씩 result에 넣는데 result에 값이 비워져 있으면 str(i)만 더하고 있으면 +까지 더한다
            if result == "":
                result += f" {i}"
            else:
                result += f" + {i}"
        print(f"{num} ={result}")
        measure_list.clear() #리스트 초기화를 안해주면 전에 값이 남아있어서 에러를 일으킨다
        result=""
    else: #완전수가 아니라면 not perfect출력
        print(f"{num} is NOT perfect.")
        measure_list.clear()