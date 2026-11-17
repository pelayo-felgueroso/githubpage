## Explanation

Diffusion Policies are a type of robot learning method that uses diffusion models to generate actions. Instead of predicting a single action directly, the model starts with random noise and gradually transforms it into a sequence of actions.

The model is trained using demonstrations of how a task should be performed. During execution, it uses observations from the robot, such as camera images or other sensor data, to generate suitable movements.

Predicting a sequence of actions allows the robot to produce smoother and more flexible behaviour. Diffusion Policies are particularly interesting for manipulation tasks, where the robot needs to interact with objects and adapt its movements to the environment.

## Resources

_Learn more from external sources._

- [Hugging Face - Diffusion Policy](https://www.youtube.com/watch?v=M03sZFfW-qU)
## Related concepts

_Explore the knowledge network._

- [[Robot Learning]]
    
- [[Imitation Learning]]
    
- [[Generative AI]]
    
- [[Perception]]
    
- [[Motion Planning]]