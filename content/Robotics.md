## Explanation

**Robotics** is a field of engineering focused on designing, building and programming robots that can interact with the physical world. It brings together different areas such as mechanical engineering, electronics, programming, control systems and artificial intelligence.

Every robot has a physical structure made of links, joints and motors, which determines how it can move and interact with its environment. This is where [[Robot Mechanics]] and [[Kinematics]] comes in. It helps us understand how the different parts of a robot move and how their positions are related.

But knowing how a robot moves is not enough. We also need to decide where it should move and how to get there. [[Motion Planning]] deals with finding a suitable path while taking obstacles and movement limitations into account. Once a path is planned, [[Robot Control]] is responsible for making the robot follow it, using sensor feedback to correct its movements when needed.

Robots also need information about their surroundings to interact with them. This is the role of [[Computer Vision]] and [[Perception]]. Using [[Cameras]] and other [[Sensors]], robots can detect objects, estimate their positions, recognise obstacles and build an understanding of the environment around them.

All these parts need to communicate with each other. Robotics Software and Integration focuses on connecting sensors, perception systems, motion planners and controllers so they can work as one system. Tools such as [[ROS 2]] make it easier to build this kind of software and connect the different components.

Another important area is teaching robots to perform tasks without having to program every single movement by hand. [[Robot Learning]] and [[Artificial Intelligence]] looks at how robots can learn from data, demonstrations and experience. This includes machine learning, reinforcement learning and imitation learning, as well as newer approaches such as [[Diffusion Policies]] and [[VLA]], which combine visual information, instructions and robot actions.

Before testing everything on a real robot, it is often useful to work in a virtual environment. [[Robot Simulation]] allows us to test robot movements, sensors and complete tasks without always needing physical hardware. However, a solution that works well in simulation does not always behave the same way in the real world. This problem is known as [[Sim-to-Real]] and is an important part of developing reliable robotic systems.

In practice, all these areas are connected. For example, imagine a robot that needs to pick up a bottle from a table. It first needs to detect the bottle and estimate its position, then calculate how to reach it, plan a suitable movement and control its motors and gripper to pick it up. Each step involves a different part of robotics, but they all need to work together to complete the task.
## Resources

_Learn more from external sources._

## Related concepts

_Explore the knowledge network._

- [[Perception]]
    
- [[Motion Planning]]
    
- [[Camera]]
    
- [[Gripper]]
      
- [[Coordinate Transformation]]
    
- [[Imitation Learning]]
    
- [[Control]]
      
- [[Robot Simulation]]
 
