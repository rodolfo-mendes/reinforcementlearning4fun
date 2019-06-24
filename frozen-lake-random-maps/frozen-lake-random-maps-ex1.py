# frozen-lake-random-maps-ex1.py
import gym # loading the Gym library

env = gym.make("FrozenLake-v0", desc=None, map_name=None) # creating the FrozenLake environment
env.reset()                     # reseting the environment to its initial state
env.render()                    # prints the environment state to the standard output
