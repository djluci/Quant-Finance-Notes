import numpy as np
rng = np.random.default_rng(52) # a simulated coin
heads = rng.random(1000) < 0.5 # a fair coin
step = np.where(heads, 1, -1) # up or down $1
price = 100 + step.cumsum() # the random walk
p = 19 / 37 # the casino edge
drift = p * 1 + (1 - p) * -1 # +2.7 cents
up = rng.random((1000, 4000)) < p # 1,000 prices
walks = np.where(up, 1, -1) 
below = (walks < 0).mean(axis=0) # below start
print(price.max(), price.min(), price[-1]) 
print(round(drift, 4), below[[24, 999, 3999]])

## What exactly is a random walk?
# A sum of coin flips, and it can look just like a stock chart

## What does the drift do?
# Barely visible in the short run, it decides the long run
