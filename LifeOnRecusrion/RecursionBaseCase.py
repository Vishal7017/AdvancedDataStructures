# define your sum_to_one() function above the function call
def sum_to_one(n):
  result = 1
  call_stack = []
  while n is not 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  return result, call_stack



sum_to_one(4)