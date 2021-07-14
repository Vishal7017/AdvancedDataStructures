def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit

# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)


