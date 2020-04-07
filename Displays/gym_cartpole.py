import cma
import gym
import numpy as np
from fixed_structure_nn_numpy import SimpleNeuralControllerNumpy
from myCMA import launch_cmaes_full, launch_cmaes_full_genotype

env = gym.make('CartPole-v1')

def eval_nn(genotype, render=True):
    total_reward=0
    nn=SimpleNeuralControllerNumpy(4,1,2,5)
    nn.set_parameters(genotype)
    observation = env.reset()
    for t in range(1000):
        if render:
            env.render()
        action=nn.predict(observation)
        if action>0:
            action=1
        else:
            action=0
        observation, reward, done, info = env.step(action)
        total_reward+=reward
        if done:
            print("Episode finished after %d timesteps"%(t+1))
            break
    return -total_reward
sigma = 1
### A completer pour optimiser les parametres du reseau de neurones avec CMA-ES ###

nn=SimpleNeuralControllerNumpy(4,1,2,5)
nn.init_random_params()
res = launch_cmaes_full_genotype(nn.get_parameters(), sigma, nbeval=1000, display=True, ma_func=eval_nn)
nn.set_parameters(res)


env.reset()

r = env.step(env.action_space.sample()) # take a random action
observations = r[0]
reward = r[1]
done = r[2]
print(nn.predict(observations))
for _ in range(1000):
    env.render()
    action = nn.predict(observations)
    if action > 0:
        action = 1
    else:
        action = 0
    r = env.step(action)  # take a random action
    observations = r[0]
    reward = r[1]
    done = r[2] # take a random action
env.close()


