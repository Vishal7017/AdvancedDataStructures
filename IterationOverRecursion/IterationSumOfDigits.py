#!/usr/bin/env python3



# def sum_digits(n):
# 	if n < 0:
# 		ValueError("Input 0 or greater only!")
# 	result = 0
# 	while n != 0:
# 		result += n % 10
# 		n = n // 10
# 	return result + n




# def sum_of_digits(n):
# 	if n < 0:
# 		ValueError("Inputs 0 or greater only!")
	
# 	result = 0

# 	while n is not 0:
# 		result += n % 10
# 		n = n // 10
# 	return result




def sum_of_digits(n):
	if n <= 9:
		return n
	last_digit = n % 10
	return sum_of_digits(n//10) + last_digit


print(sum_of_digits(12))
print(sum_of_digits(552))
print(sum_of_digits(123456789))