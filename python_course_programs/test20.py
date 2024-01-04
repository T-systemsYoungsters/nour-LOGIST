import random
'''

def fibonacci_series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
''' 
def fibonacci_series(n, memo=[0, 1]):
    if len(memo) > n:
        return memo[n]
    else:
        for i in range(len(memo), n + 1):
            result = memo[i - 1] + memo[i - 2]
            memo.append(result)
        return memo[n]


score = 41237
highscore = 1023407

print("Sorce:  {:>14,} ".format(score))
print("High score: {:10,} ".format(highscore))


for i in range(1,21):
    print("1/{:<2} = {:.3}".format(i,1/i))

for i in range(1,36):
    print("{:>2} - {:>11,}".format(i,fibonacci_series(i)))
 