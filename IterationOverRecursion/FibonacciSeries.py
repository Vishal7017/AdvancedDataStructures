#!/usr/bin/env python3

def fibonacci(n):
	if n <= 0:
		ValueError("Enter number greater than zero")
	fibs = [0, 1]
	if n <= len(fibs) - 1:
		return fibs[n]
	
	while n > len(fibs) - 1:
		fibs.append(fibs[-1] + fibs[-2])
	return fibs[-1]
	
	
	
	
	