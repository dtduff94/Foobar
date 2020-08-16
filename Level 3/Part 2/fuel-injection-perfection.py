def solution(n):
  n = int(n)
  ops = 0
  
  while n > 1:
    if n % 2 == 0:
      n = n / 2
    else:
      if ((n == 3) or (n % 4 == 1)):
        n -= 1
      else:
        n += 1

    ops += 1
  return ops
