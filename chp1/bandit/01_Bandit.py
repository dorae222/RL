import numpy as np

# Bandit is Slot Machine
class Bandit:
    # 슬롯 머신 초기화
    def __init__(self, arms=10):
        # Random win rate
        self.rates = np.random.rand(arms)

    # 승률과 난수 간의 비교
    def play(self,arm):
        rate = self.rates[arm]
        # Compare win rate with random num
        if rate > np.random.rand():
            return 1
        else:
            return 0