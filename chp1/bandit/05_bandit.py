import numpy as np
import matplotlib.pyplot as plt


class Bandit:
    def __init__(self, arms=10): 
        self.rates = np.random.rand(arms)  # 슬롯머신 각각의 승률 설정(무작위)

    def play(self, arm):
        rate = self.rates[arm]
        if rate > np.random.rand():
            return 1
        else:
            return 0


class Agent:
    def __init__(self, epsilon, action_size=10):
        self.epsilon = epsilon  # 무작위로 행동할 확률(탐색 확률)
        self.Qs = np.zeros(action_size)
        self.ns = np.zeros(action_size)

    # 슬롯머신의 가치 추정
    def update(self, action, reward):
        self.ns[action] += 1
        self.Qs[action] += (reward - self.Qs[action]) / self.ns[action]

    # 행동 선택(ε-탐욕 정책)
    def get_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.Qs))  # 무작위 행동 선택
        return np.argmax(self.Qs)  # 탐욕 행동 선택


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
