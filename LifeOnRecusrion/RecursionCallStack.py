def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n-1)
  

  
print(sum_to_one(7))

# def sum_to_one(n):
#     result = 1
#     call_stack = []
#     while n != 1:
#         execution_context = {"n_value": n}
#         call_stack.append(execution_context)
#         n -= 1
#         print(call_stack)
#     print("BASE CASE RECAHED")
#     return result, call_stack

# sum_to_one(10)



