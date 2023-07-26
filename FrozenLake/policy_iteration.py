import gym
import numpy as np

def policy_iteration(P, nS, nA, gamma=0.9, tol=1e-4):
    '''
    parameters:
        P: transition probability matrix
        nS: number of states
        nA: number of actions
        gamma: discount factor
        tol: tolerance for convergence
    returns:
        value_function: value function for each state
        policy: policy for each state
    '''
    # initialize value function and policy
    value_function = np.zeros(nS)
    policy = np.zeros(nS, dtype=int)

    # Implement policy iteration here #
    
    pass
    return value_function, policy

if __name__ == "__main__":
    
    # create FrozenLake environment note that we are using a deterministic environment change is_slippery to True to use a stochastic environment
    env = gym.make("FrozenLake-v1", is_slippery=False)
    # reset environment to start state
    env.reset()
    # run policy iteration algorithm
    # value_function, policy = policy_iteration(env.P, env.nS, env.nA, gamma=0.9, tol=1e-4)
    print(env.observation_space)
    