# 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

def solution(orders, course):
  answer = []
  arrs = []
  orders = [sorted(order) for order in orders]

  for i in course:
    for j in orders:
      arrs += list(combinations(list(j), i))
   
    if len(arrs) < 1: break
    new_dict = dict(Counter(arrs)) 
    max_value = max(new_dict.values())
    result = [k for k, v in new_dict.items() if v == max_value and v != 1]

    for ch in result:
      answer.append(''.join(list(ch)))
    arrs = []

  return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))