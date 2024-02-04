import numpy as np
import matplotlib.pyplot as plt


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

class Agent:
    # 에이전트 초기화
    def __init__(self, epsilon, action_size=10):
        self.epsilon = epsilon  # 탐험을 위한 epsilon 값 설정
        self.Qs = np.zeros(action_size)  # 각 행동의 가치를 저장할 배열 초기화
        self.ns = np.zeros(action_size)  # 각 행동이 선택된 횟수를 저장할 배열 초기화

    # 에이전트의 행동 가치 업데이트
    def update(self, action, reward):
        self.ns[action] += 1  # 선택된 행동의 카운트 증가
        # 선택된 행동의 가치(Q)를 업데이트하는 공식: Q = Q + (보상 - Q) / n
        self.Qs[action] += (reward - self.Qs[action]) / self.ns[action]

    # 에이전트의 행동 선택
    def get_action(self):
        if np.random.rand() < self.epsilon:
            # epsilon 확률로 무작위 행동 선택
            return np.random.randint(0, len(self.Qs))
        # 그렇지 않으면 현재 가장 가치가 높은 행동 선택
        return np.argmax(self.Qs)



if __name__ == '__main__':
    simulations = 10
    steps = 1000
    epsilon = 0.1

    all_total_rewards = []  # 모든 시뮬레이션의 누적 보상 저장
    all_rates = []  # 모든 시뮬레이션의 승률 저장

    for sim in range(simulations):
        bandit = Bandit()
        agent = Agent(epsilon)
        total_rewards = []  # 현재 시뮬레이션의 누적 보상
        rates = []  # 현재 시뮬레이션의 승률

        for step in range(steps):
            action = agent.get_action()
            reward = bandit.play(action)
            agent.update(action, reward)
            
            if step == 0:
                total_rewards.append(reward)
            else:
                total_rewards.append(total_rewards[-1] + reward)  # 누적 보상 업데이트
            rates.append(total_rewards[-1] / (step + 1))  # 승률 계산

        all_total_rewards.append(total_rewards)
        all_rates.append(rates)

    plt.figure(figsize=(14, 6))

    # 단계별 누적 보상 그래프
    plt.subplot(1, 2, 1)
    plt.title("Total Rewards Over Steps")
    plt.xlabel("Steps")
    plt.ylabel("Total Rewards")
    for i, sim_rewards in enumerate(all_total_rewards):
        plt.plot(sim_rewards, alpha=0.6, label=f'Simulation {i+1}')

    plt.legend()

    # 단계별 승률 그래프
    plt.subplot(1, 2, 2)
    plt.title("Winning Rate Over Steps")
    plt.xlabel("Steps")
    plt.ylabel("Winning Rate")
    for i, sim_rates in enumerate(all_rates):
        plt.plot(sim_rates, alpha=0.6, label=f'Simulation {i+1}')

    plt.legend()

    plt.tight_layout()
    plt.show()
