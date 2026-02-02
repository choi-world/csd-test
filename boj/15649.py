# N과 M (1)
# https://www.acmicpc.net/problem/15649

from itertools import permutations

N, M = map(int, input().split()) # N이 배열, M이 선택
arr = list(range(1, N + 1))

for item in list(permutations(arr, M)):
  print(' '.join(map(str, item)))