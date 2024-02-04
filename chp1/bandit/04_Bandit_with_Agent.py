import matplotlib.pyplot as plt
from Bandit import *
from Agent import *

np.random.seed(0) # Fixed Seed

# 시뮬레이션 설정
steps = 1000 # 총 시행 횟수
epsilon = 0.1 # 탐험을 위한 epsilon 값
rates = list() # 승률 저장용 리스트

# 객체 선언
bandit = Bandit()
agent = Agent(epsilon)

total_reward = 0
total_rewards = list() # reward 저장용 리스트

for step in range(steps):
    action = agent.get_action() # 1) 행동의 가치 반환
    reward = bandit.play(action) # 2) 실제로 play이후 reward
    agent.update(action, reward) # 3) action value와 reward로 학습
    total_reward += reward

    total_rewards.append(total_reward)
    rates.append(total_reward/(step+1))

print("total_reward:", total_reward)

# # 단계별 보상 가치 총합
# plt.ylabel('Total reward')
# plt.xlabel('Steps')
# plt.plot(total_rewards)
# plt.show()

# 단계별 누적 보상 가치 비율
plt.ylabel('Rates')
plt.xlabel('Steps')
plt.plot(rates)
plt.show()