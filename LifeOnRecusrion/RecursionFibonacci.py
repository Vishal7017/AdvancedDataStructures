# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  return fibonacci(n-1) + fibonacci(n -2)


fibonacci(5)
# set the appropriate runtime:

# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"


# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  return fibonacci(n-1)+fibonacci(n-2)



print(fibonacci(9))
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"