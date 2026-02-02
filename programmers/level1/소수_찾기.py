# 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
  temp = [True] * (n + 1)
  temp[0] = False
  temp[1] = False

  for i in range(2, int(len(temp) ** 0.5) + 1):
    if temp[i]:
      for j in range(i * 2, len(temp), i):
        temp[j] = False

  return temp.count(True)

print(solution(10))
print(solution(5))