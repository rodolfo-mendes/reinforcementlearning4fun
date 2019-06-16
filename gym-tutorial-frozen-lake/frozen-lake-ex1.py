# frozen-lake-ex1.py
import gym # loading the Gym library

env = gym.make("FrozenLake-v0") # creating the FrozenLake environment
env.reset()                     # reseting the environment to its initial state
env.render()                    # prints the environment state to the standard output

print("Action space: ", env.action_space)           # prints the action space
print("Observation space: ", env.observation_space) # prints the observation space
