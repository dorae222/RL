import numpy as np

np.random.seed(0) # Fixed Seed
rewards = list()

# N = 10
for n in range(1,11):
    # Random Reward
    reward = np.random.rand()
    rewards.append(reward)
    Q = sum(rewards)/n
    print(f"{n} Reward Avg:",'\n',Q,'\n')