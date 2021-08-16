# Define sum_to_one() below...
def sum_to_one(n):
  if n == 0:
    return 0
  print("Recursing with input: {0}".format(n))
  return sum_to_one(n-1)+ n


# uncomment when you're ready to test
print(sum_to_one(7))

def sum_to_one(n):
  if n is 1:
    return n
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n-1)

print(sum_to_one(18))