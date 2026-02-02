# N과 M (3)
# https://www.acmicpc.net/problem/15651

N, M = map(int, input().split()) # N이 배열, M이 선택
arr = list(range(1, N + 1))
result = []

def permutations(level):
  if level == M:
    print(*result)
    return

  for i in range(0, len(arr)):
    result.append(arr[i])
    permutations(level + 1)
    result.pop()

permutations(0)