def calculate_min_cost(n, distances, prices):
    total_cost = 0
    min_price = prices[0]  # 가장 싼 가격을 초기화
    for i in range(n - 1):  # 마지막 도시의 경우 제외
        total_cost += min_price * distances[i]  # 현재 도시까지 가장 싼 가격으로 기름을 넣는다
        min_price = min(min_price, prices[i + 1])  # 다음 도시의 기름 가격과 비교하여 더 싼 가격으로 바꿈
    return total_cost

# 입력 받기
n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 최소 비용 계산 및 출력
min_cost = calculate_min_cost(n, distances, prices)
print(min_cost)