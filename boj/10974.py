# 모든 순열
# https://www.acmicpc.net/problem/10974

N = int(input())
result = []
arr = list(range(1, N + 1))
check = [False] * (N + 1)

def permutation(level):
  if level == N:
    print(*result)
    return

  for i in range(0, len(arr)):
    if check[i]: continue

    result.append(arr[i])
    check[i] = True

    permutation(level + 1)
    check[i] = False
    result.pop()

permutation(0)