# 칸토어 집합
# https://www.acmicpc.net/problem/4779

""" 재귀
3 : ---------------------------
2 : ---------         ---------
1 : ---   ---         ---   ---
0 : - -   - -         - -   - -
"""

""" 메모이제이션
0 : -
1 : - -
2 : - -   - -
3 : - -   - -         - -   - -

arr[0] = '-'
arr[1] = arr[0] + ' ' * (3 ** (1 - 1)) + arr[0]
arr[2] = arr[1] + ' ' * (3 ** (2 - 1)) + arr[1]
arr[i] = arr[i - 1] + ' ' * (3 ** (i - 1)) + arr[i - 1]
"""

def recursion(n):
  if (n == 0):
    print('-', end="")
    return
  
  recursion(n - 1)
  print(' ' * (3 ** (n - 1)), end="")
  recursion(n - 1)

def memoization(n):
  MAX = 12
  arr = [' '] * (MAX + 1)
  arr[0] = '-'
  
  for i in range(1, MAX + 1):
    arr[i] = arr[i - 1] + ' ' * (3 ** (i - 1)) + arr[i - 1]

  return arr[n]


while True:
  try:
    n = int(input())
    print(memoization(n))
  except:
    break