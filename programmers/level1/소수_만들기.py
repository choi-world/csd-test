# 소수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12977?language=python3

from itertools import combinations

def solution(nums):
  arr = []
  result = []
  cnt = 0
  check = is_prime()

  def combination(idx, level):
    if level == 3:
      arr.append(result[:])
      return
    
    for i in range(idx, len(nums)):
      result.append(nums[i])
      combination(i + 1, level + 1)
      result.pop()

  combination(0, 0)

  for i in range(len(arr)):
    if check[sum(arr[i])]: cnt += 1

  return cnt

def is_prime():
  arr = [True] * 10001
  arr[0] = False
  arr[1] = False

  for i in range(2, int(len(arr) ** 0.5) + 1):
    if arr[i]:
      for j in range(i * 2, len(arr), i):
        arr[j] = False

  return arr

def library(nums):
  arrs = list(combinations(nums, 3))
  check = is_prime()
  cnt = 0

  for arr in arrs:
    if check[sum(arr)]: cnt += 1
  
  return cnt

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
print(library([1, 2, 3, 4]))
print(library([1, 2, 7, 6, 4]))