cube = 64
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guessess = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guessess += 1
print('num_guessess = ', num_guessess)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)