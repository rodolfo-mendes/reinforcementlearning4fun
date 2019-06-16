# frozen-lake-ex3.py
import gym

actions = {
    'Left': 0,
    'Down': 1,
    'Right': 2, 
    'Up': 3
}

print('---- winning sequence ------ ')
winning_sequence = (2 * ['Right']) + (3 * ['Down']) + ['Right']
print(winning_sequence)

env = gym.make("FrozenLake-v0")
env.reset()
env.render()

for a in winning_sequence:
    new_state, reward, done, info = env.step(actions[a])
    print()
    env.render()
    print("Reward: {:.2f}".format(reward))
    print(info)
    if done:
        break   

print()
