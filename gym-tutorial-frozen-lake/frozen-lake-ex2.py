# frozen-lake-ex2.py
import gym

MAX_ITERATIONS = 10

env = gym.make("FrozenLake-v0")
env.reset()
env.render()
for i in range(MAX_ITERATIONS):
    random_action = env.action_space.sample()
    new_state, reward, done, info = env.step(random_action)
    env.render()
    if done:
        break   
