import numpy as np

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
