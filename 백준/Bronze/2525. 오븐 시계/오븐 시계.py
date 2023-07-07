hour, minute = map(int, input().split())  # 시간과 분을 입력받는다
plus_m = int(input())  # 요리를 하는데 필요한 시간

def timers(hour, minute, plus_m):
    if minute + plus_m >= 60:  # 현재시간에서 요리하는데 필요한 시간을 더해 60분이 넘으면 1시간 추가
        if hour == 23:  # 23시면 1시간 더하여 0시
            hour = 0
            minute = (minute + plus_m) - 60
            plus_m = 0
        else:
            hour += 1
            minute = (minute + plus_m) - 60
            plus_m = 0
        if minute >= 60:
            return timers(hour, minute, plus_m)
    else:
        minute += plus_m

    return hour, minute

final_hour, final_minute = timers(hour, minute, plus_m)
print(final_hour, final_minute)
