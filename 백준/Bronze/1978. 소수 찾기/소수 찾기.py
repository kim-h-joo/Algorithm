import math

N = int(input())
nums = list(map(int, input().split()))

cnt = 0
toggle = 0

for num in nums:
  if num == 1: continue
  toggle = 0
  mid = int(math.sqrt(num))
  for i in range(2, mid + 1):
    if num % i == 0:
      toggle = 1
      break
  if (toggle == 1): continue
  cnt += 1

print(cnt)