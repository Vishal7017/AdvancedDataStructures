def sum_to_one(n):
  result = 1
  call_stack = []
  while (n >= 1):
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  while len(call_stack) > 1:
      return_value = call_stack.pop()
      result += return_value["n_value"]
      print(result)
  return result, call_stack


print(sum_to_one(12))