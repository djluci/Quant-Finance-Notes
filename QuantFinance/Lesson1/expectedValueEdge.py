import numpy as np
rng = np.random.default_rng(7) #simulated wheel
p = 18/37 # red : 18 of 37
ev = p * 1 + (1 - p) * -1 #expected value
spins = rng.random((1000, 1000)) # 1000 players
pn1 = np.where(spins < p, 1, -1) # win or lose $1
paths = pn1.cumsum(axis=1) # every balance
final = spins[:, -1] # after 1000 spins
winners = (final > 0).sum() # players ahead
casino = -pn1.sum() # the house side
per_bet = casino / pn1.size # edge per bet
print(round(ev, 4), winners, casino, per_bet)

## What is an edge
# a small positive expected value

## why does it become certain 
# The edge grows with every bet, luck only with its square root