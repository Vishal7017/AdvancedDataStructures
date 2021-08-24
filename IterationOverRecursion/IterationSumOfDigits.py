#!/usr/bin/env python3

def sum_digits(n):
	if n < 0:
		ValueError("Input 0 or greater only!")
	result = 0
	while n != 0:
		result += n % 10
		n = n // 10
	return result + n

print(sum_digits(12))
print(sum_digits(552))
print(sum_digits(123456789))