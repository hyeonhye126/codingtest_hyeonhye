N = int(input())

year = 2024
month = 8

# N번째는 (N-1) * 7 개월 후
total_months = month + (N - 1) * 7

# year와 month를 갱신
year += (total_months - 1) // 12
month = (total_months - 1) % 12 + 1

print(year, month)