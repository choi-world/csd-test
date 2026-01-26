# 조합 알고리즘 이해하기
"""
조합은 순서를 따지지 않고 나열할 수 있는 경우의 수를 말한다.

반복문으로 먼저 구현해보면 다음과 같다.
"""
for a in range(1, 11):
  for b in range(a + 1, 11):
    for c in range(b + 1, 11):
      for d in range(c + 1, 11):
        for e in range(d + 1, 11):
          print(a, b, c, d, e)

"""
이렇게 구할 수 있지만 시간 복잡도가 굉장히 높아지기에 알맞은 풀이방법은 아니라고 볼 수 있다.
이를 재귀 형식으로 다시 구현해보겠다.
"""

result = []
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def combination(idx, level):
  if level == 5:
    print(result)
    return

  for i in range(idx, 10):
    result.append(arr[i])
    combination(i + 1, level + 1)
    result.pop()
    
"""
combination(0, 0) - result: [1], 아직 return x
combination(1, 1) - result: [1, 2], 아직 return x
combination(2, 2) - result: [1, 2, 3], 아직 return x
combination(3, 3) - result: [1, 2, 3, 4], 아직 return x
combination(4, 4) - result: [1, 2, 3, 4, 5], 아직 return x
combination(5, 5) - print(result), return
combination(4, 4) - result: [1, 2, 3, 4, 6], 아직 return x
combination(5, 5) - print(result), return
combination(4, 4) - result: [1, 2, 3, 4, 7], 아직 return x
...
"""

print(combination(0, 0))