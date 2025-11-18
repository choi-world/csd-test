# 거스름돈

"""
거슬러줘야 할 동전의 최소 개수 -> 가장 큰 수로 나누어 그 몫을 더한다.
존재하는 돈은 500, 100, 50, 10원 -> 1600원이면 500 * 3 + 100 * 1이 되므로 4가 된다.
"""

n = int(input())
result = 0

coins = [500, 100, 50, 10]
for coin in coins:
    result += (n // coin)
    n %= coin

print(result)