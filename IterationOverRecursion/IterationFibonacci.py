def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  fibs = [0, 1]
  if n <= len(fibs) - 1:
    return fibs[n]
  while n > len(fibs) - 1:
    fibs.append(fibs[-1] + fibs[-2])
  return fibs[-1]