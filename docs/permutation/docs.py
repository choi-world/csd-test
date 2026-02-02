# 순열 알고리즘 이해하기
"""
조합과 다르게 순열은 순서를 고려하여 나열할 수 있는 경우의 수를 말한다.
"""
for i in range(1, 11):
  for j in range(1, 11):
    for k in range(1, 11):
      if i != j and j != k and i != k:
        print(i, j, k)

"""
마찬가지로 많은 for문이 반복되기 때문에 재귀로 이를 처리하는 것이 올바르다.
"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [False] * len(arr)
result = []

def permutation(level):
  if level == 3:
    print(result)
    return

  for i in range(0, len(arr)):
    if check[i]: continue

    result.append(arr[i])
    check[i] = True
    permutation(level + 1)

    check[i] = False
    result.pop()

permutation(0)

"""
permuation(0) - result: [1], check[0]: True
permutation(1) - result: [1, 2], check[1]: True
permutation(2) - result: [1, 2, 3], check[2]: True
permutation(3) - print(result), 해당 함수 종료
permutation(2) - check[2]: False, result.pop(), result: [1, 2]
permutation(2) - result: [1, 2, 4], check[3]: True
...
"""