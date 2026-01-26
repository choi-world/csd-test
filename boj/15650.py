# N과 M (2)
# https://www.acmicpc.net/problem/15650

N, M = map(int, input().split())
result = []
arr = list(range(1, N + 1))

def combination(idx, level):
  if level == M:
    print(*result)
    return

  for i in range(idx, len(arr)):
    result.append(arr[i])
    combination(i + 1, level + 1)
    result.pop()

combination(0, 0)