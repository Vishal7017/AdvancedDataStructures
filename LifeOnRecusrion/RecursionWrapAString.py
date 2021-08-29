# define wrap_string() here
def wrap_string(wrap, i):
  result = ""
  if i <= 0:
    return wrap
  result += "<"
  result += wrap_string(wrap, i-1)
  result += ">"
  return result
# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)