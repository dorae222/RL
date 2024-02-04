import numpy as np

np.random.seed(0) # Fixed Seed
rewards = list()

# Q: 행동 가치 추정치
# 표본 평균
Q = 0

# N = 10
for n in range(1,11):
    # Random Reward
    reward = np.random.rand()
    # Update Sample Mean
    Q = Q + (reward-Q) / n
    # Q += (reward-Q) / n
    print(f"{n} Reward Avg:",'\n',Q)

'''
1 Reward Avg: 
 0.5488135039273248
2 Reward Avg:
 0.6320014351498722
3 Reward Avg:
 0.6222554154571294
4 Reward Avg:
 0.6029123573420713
5 Reward Avg:
 0.567060845741438
6 Reward Avg:
 0.5801997236289743
7 Reward Avg:
 0.5598265075766483
8 Reward Avg:
 0.6013198192273272
9 Reward Avg:
 0.6415801460355164
10 Reward Avg:
 0.6157662833145425
'''