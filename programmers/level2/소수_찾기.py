# 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
  answer = 0
  arr = []
  
  for i in range(1, len(list(numbers)) + 1):
    for item in permutations(list(numbers), i):
      arr.append("".join(list(item)))

  arr = list(set(list(map(int, arr))))
  prime = [True] * (max(arr) + 1)
  prime[0] = False
  prime[1] = False
  
  for i in range(2, int(len(prime) ** 0.5) + 1):
    if prime[i]:
      for j in range(i * 2, len(prime), i):
        prime[j] = False

  for i in arr:
    if prime[i]: answer += 1

  return answer

print(solution("17"))
print(solution("011"))