def is_palindrome(my_string):
    while len(my_string) > 1:
        if my_string[0] != my_string[-1]:
            return False
        my_string = my_string[1:-1]
    return True


print(is_palindrome("abba"))
print(is_palindrome("abccba"))
print(is_palindrome("dance"))