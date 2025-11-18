# 숫자 카드 게임

"""
n, m을 입력받음. m은 행, n은 열을 의미한다.
m의 개수만큼 입력받고 여기서 가장 작은 수를 열 별로 따져 그 중 가장 큰 수를 리턴
"""

n, m = map(int, input().split())
result = 0

for i in range(n):
    arr = list(map(int, input().split()))
    result = min(arr) if result < min(arr) else result

print(result)