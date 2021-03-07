from itertools import combinations
def is_prime_number(x):
  # 2부터 (x - 1)까지의 모든 수를 확인
  for i in range(2, x):
  	# x가 해당 수로 나누어떨어지면
    if x % i == 0:
    	return False
  return True

def solution(nums):
    answer = 0
    sub = []
    for i in list(combinations(nums, 3)):
        a, b, c = i
        sub.append(a+b+c)

    for i in sub:
        if is_prime_number(i) == True:
            answer += 1

    return answer