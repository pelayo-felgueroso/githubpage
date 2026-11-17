## Explanation

Robot Learning is the use of machine learning techniques to help robots acquire skills and improve their behaviour through data and experience.

Instead of programming every movement manually, a robot can learn how to perform tasks from demonstrations, interaction with the environment or simulated experience.

Different approaches are used depending on the problem. [[Imitation Learning]] allows robots to learn from demonstrations, while reinforcement learning uses rewards to guide the learning process. Other methods combine visual information, language instructions and robot actions.

Robot learning is particularly useful for complex tasks such as object manipulation, where the environment and object positions can change between attempts.

The learning process usually requires data collection, training, evaluation and deployment. A model that performs well during training may still fail in a new environment, so testing and adapting it on real hardware are important steps.

A trained model can be deployed on a physical robot, although differences between simulation and reality can affect its performance. This is known as the [[Sim-to-Real]] problem.

## Resources

_Learn more from external sources._

- [Hugging Face – LeRobot Documentation](https://huggingface.co/docs/lerobot/en/index)
    
- [NVIDIA Isaac Lab – Documentation](https://isaac-sim.github.io/IsaacLab/)
    
- [NVIDIA – Physical AI and Robotics Learning](https://docs.nvidia.com/learning/physical-ai/robotics.html)
    
## Related concepts

_Explore the knowledge network._

- [[Robotics]]
    
- [[Machine Learning]]
    
- [[Imitation Learning]]
    
- [[Diffusion Policies]]
    
- [[VLA]]
    
- [[Robot Simulation]]
    
- [[Sim-to-Real]]