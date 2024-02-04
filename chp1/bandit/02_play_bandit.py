from Bandit import *

# Bandit 객체 선언
bandit = Bandit()

for i in range(3):
    print(f"{i}번째 보상여부",bandit.play(0))