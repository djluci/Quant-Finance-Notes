import numpy as np
rng = np.random.default_rng(3) # simulated coin
coin = [1, -1]
steps = rng.choice(coin, (1000, 400)) # 400 each
walks = steps.cumsum(axis=1) # 1,000 prices
spread = walks.std(axis=0) # typical distance
print(spread[[24, 99, 399]]) # about 5, 10, 20
print(np.sqrt([35, 100, 400])) # 5, 10, 20
var = spread ** 2
near = (abs(walks[:, 99]) <= 10).mean() # 73%
print(var[99], near) # 100, root 10
n = np.array([25, 4000]) # part two's steps
print(n / 37, np.sqrt(n)) # drift, randomness
days = 0.01 * rng.choice(coin, (2000, 252))
yearly = 0.01 * np.sqrt(252) # 16 % a year
print(yearly, (abs(days.sum(1)) <= yearly).mean())

# Why is it important 
# Risk grows with the square root of time: 100 random steps take you about 10 away, and daily risk turns into yearly risk

# What does it mean for a stock?
# 1% a day becomes about 16% a year, and with a positive drift, going up gets more likely over time