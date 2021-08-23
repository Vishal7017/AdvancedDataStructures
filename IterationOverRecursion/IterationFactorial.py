def factorial(n):
  if n < 0:
    ValueError("Inputs 0 or greater only")
  if n <= 1:
    return 1
  result = 1
  while n != 1:
    result = result * n
    n = n - 1
  return result

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)