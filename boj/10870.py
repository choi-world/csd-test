# 피보나치 수
# https://www.acmicpc.net/problem/10870

n = int(input())

def fibonacci(n):
  if (n == 0): return 0
  elif (n <= 2): return 1

  return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(n))

def memoization(n):
  MAX = 20
  arr = [0] * (MAX + 1)

  arr[1] = 1
  arr[2] = 1

  for i in range(3, len(arr)):
    arr[i] = arr[i - 2] + arr[i - 1]
  
  return arr[n]

# print(memoization(n))

def memonacci(n):
  global arr

  if (arr[n] != -1): return arr[n]
  arr[n] = memonacci(n - 2) + memonacci(n - 1)
  return arr[n]


MAX = 20
arr = [-1] * (MAX + 1)
arr[0] = 0
arr[1] = 1

print(memonacci(n))