# 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
  answer = []
  temp = k
  # k는 유저의 피로도, dungeons는 ["최소 필요 피로도", "소모 피로도"]
  
  for items in list(permutations(dungeons, len(dungeons))):
    count = 0
    temp = k

    for item in items:
      if temp >= item[0]: 
        temp -= item[1]
        count += 1
    answer.append(count)

  return max(answer)

print(solution(80, [[80, 20], [50, 40], [30, 10]]))