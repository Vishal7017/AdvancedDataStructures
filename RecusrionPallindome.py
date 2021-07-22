def is_palindrome(str):
  if len(str) < 2:
    return True
  if str[0] != str[-1]:
    return False
  return is_palindrome(str[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)