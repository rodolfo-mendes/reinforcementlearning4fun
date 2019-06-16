# frozen-lake-ex5.py
import gym

print("\n--- 8x8 map by env id ---")
env = gym.make("FrozenLake8x8-v0")
env.reset()
env.render()

print("\n--- 8x8 map by map_name parameter ---")
env = gym.make('FrozenLake-v0', map_name='8x8')
env.reset()
env.render()

print('\n--- custom 5x5 map ---')
custom_map = [
    'SFFHF',
    'HFHFF',
    'HFFFH',
    'HHHFH',
    'HFFFG'
]

env = gym.make('FrozenLake-v0', desc=custom_map)
env.reset()
env.render()
