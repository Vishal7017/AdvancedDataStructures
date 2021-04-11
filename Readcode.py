s = [88, 92, 76, 43, 23]
print(sum(s)/len(s))

s1 = [x ** 0.5 *10 for x in s]
print(sum(s1)/len(s))


import math
import numpy as np 

test_scores = [88, 32, 53, 23, 86]
print(np.mean(test_scores))

curved_5 = [score + 5 for score in test_scores]
print(np.mean(curved_5))

curved_10 = [score + 10 for score in test_scores]
print(np.mean(curved_10))

curved_sqrt = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_sqrt))