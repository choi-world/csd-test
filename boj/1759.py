# 암호 만들기
# https://www.acmicpc.net/problem/1759

L, C = map(int, input().split())
arr = sorted(list(map(str, input().split())))
result = []

def check(arr):
  vows = set('aeiouAEIOU')
  vow = 0 # 모음
  cons = 0 # 자음

  for ch in arr:
    if ch in vows: vow += 1
    else: cons += 1

  return vow >= 1 and cons >= 2

def combination(idx, level):
  if level == L:
    if check(result): print("".join(map(str, result)))
    return

  for i in range(idx, C):
    result.append(arr[i])
    combination(i + 1, level + 1)
    result.pop()

combination(0, 0)