import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")

# Initialize the environment
observation, info = env.reset()

# Run the simulation loop
for _ in range(1000):
    env.render()
    
    action = env.action_space.sample()  # Sample random action
    observation, reward, done, truncated, info = env.step(action)  # Take a step
    
    if done or truncated:
        observation, info = env.reset()  # Reset the environment if done

env.close()