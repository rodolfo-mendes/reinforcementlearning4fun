# frozen-lake-random-maps-ex2.py
import gym
from gym.envs.toy_text.frozen_lake import generate_random_map

random_map = generate_random_map(size=20, p=0.8)

env = gym.make("FrozenLake-v0", desc=random_map)
env.reset()
env.render()
