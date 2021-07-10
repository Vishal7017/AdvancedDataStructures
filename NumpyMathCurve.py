# s = [88, 92, 76, 43, 23]
# print(sum(s)/len(s))

# s1 = [x ** 0.5 *10 for x in s]
# print(sum(s1)/len(s))


# import math
# import numpy as np 

# test_scores = [88, 32, 53, 23, 86]
# print(np.mean(test_scores))

# curved_5 = [score + 5 for score in test_scores]
# print(np.mean(curved_5))

# curved_10 = [score + 10 for score in test_scores]
# print(np.mean(curved_10))

# curved_sqrt = [math.sqrt(score) * 10 for score in test_scores]
# print(np.mean(curved_sqrt))

# But Better

import math
import numpy as np 

def flat_curve(arr, n):
    return [i + n for i in arr]

def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]

test_scores = [88, 92, 79, 93, 85]
curved_5 = flat_curve(test_scores, 5)
curved_10 = flat_curve(test_scores, 10)
curved_sqrt = square_root_curve(test_scores)

for score_list in test_scores, curved_5, curved_10, curved_sqrt:
    print(np.mean(score_list))