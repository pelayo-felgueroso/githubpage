## Explanation

Imitation Learning is a machine learning approach where a model learns to perform a task by observing demonstrations from an expert, usually a human or another controller.

In robotics, a human can control a robot through teleoperation and demonstrate how a task should be performed. The system records observations and actions, which are then used to train a policy.

The trained policy learns to associate the current state of the environment with the actions needed to perform the task. For example, it can learn how to move a robot arm towards an object, grasp it and place it somewhere else.

One common approach is behavioural cloning, where the model learns to reproduce the actions shown in the demonstrations. Other approaches use demonstrations together with additional learning methods to improve performance.

Imitation learning is useful when manually programming every movement would be difficult. However, the model can struggle when it encounters situations that are very different from the demonstrations it was trained on. The quality and variety of the collected data are therefore important.

## Resources

_Learn more from external sources._

- [Hugging Face – LeRobot Documentation](https://huggingface.co/docs/lerobot/en/index)
    
- [Hugging Face – LeRobot Imitation Learning](https://huggingface.co/docs/lerobot/il_robots)
    
- [OpenVLA – GitHub Repository](https://github.com/openvla/openvla)
    

## Related concepts

_Explore the knowledge network._

- [[Robot Learning]]
    
- [[Diffusion Policies]]
    
- [[Neural Networks]]
    
- [[Perception]]
    
- [[VLA]]