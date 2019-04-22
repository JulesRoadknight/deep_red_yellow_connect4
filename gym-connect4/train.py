import gym
env = gym.make('gym_connect4:connect4-v0')

for i_episdoes in range(1000):
    env.reset()
    for t in range(42):
        obs, reward, done = env.step(env.action_space.sample())
        print(obs)
        if done :
            print('Episode Finished after {} turns'.format(t+1))
            break
env.close()
