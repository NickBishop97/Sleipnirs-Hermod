import gym

# OpenAI gym research spike into the possiblity of simulating real time data for Hermod DDS
# To be read by the sensors and published rather than generating random data to publish.
env = gym.make('MountainCarContinuous-v0',render_mode="rgb_array")

env.action_space.seed(42)

observation, info = env.reset(seed=42, return_info=True)

for _ in range(1000):
    observation, reward, done, info = env.step(env.action_space.sample())
    print(observation)

    if done:
        observation, info = env.reset(return_info=True)

env.close()