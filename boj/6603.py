# 로또
# https://www.acmicpc.net/problem/6603

def combination(idx, level):
  global result
  if level == selected:
    print(" ".join(map(str, result)))
    return

  for i in range(idx, len(arr)):
    result.append(arr[i])
    combination(i + 1, level + 1)
    result.pop()

while True:
  inserted = list(map(int, input().split()))
  n = inserted[0]
  arr = inserted[1:]
  selected = 6
  result = []

  if n == 0: break
  combination(0, 0)
  print()