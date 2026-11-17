## Explanation

Motion Planning is the process of finding a path or trajectory that allows a robot to move from an initial configuration to a target configuration while avoiding obstacles and respecting its movement constraints.

A robot needs information about its current state, the environment and the target it wants to reach. A planning algorithm uses this information to find a suitable movement.

Motion planning can take place in different spaces. In joint space, the planner searches for valid configurations of the robot's joints. In Cartesian space, it plans the movement of the end effector through the workspace.

Common planning algorithms include RRT, RRT* and PRM. They explore the space of possible movements to find a path that connects the start and target configurations without collisions.

A path only describes where the robot should move. To execute it, the system usually needs to generate a trajectory that also considers time, velocity and acceleration limits.

Motion planning is used in robotic manipulation, navigation and industrial automation. For example, a robot arm can use it to reach an object while avoiding other objects on a table.

## Resources

_Learn more from external sources._

- [Mike Likes Robots – Getting Started with MoveIt](https://www.youtube.com/watch?v=yIVc5Xq0Xm4&t=3021s)
     
- [MoveIt 2 – Motion Planning Concepts](https://moveit.ai/documentation/concepts/)
    
- [MoveIt 2 – Motion Planning Pipeline Tutorial](https://moveit.picknik.ai/main/doc/examples/motion_planning_pipeline/motion_planning_pipeline_tutorial.html)
## Related concepts

_Explore the knowledge network._

- [[Robotics]]
    
- [[Kinematics]]
    
- [[Inverse Kinematics]]
    
- [[Jacobian Matrix]]
    
- [[Robot Simulation]]
    
- [[Robot Learning]]
    
- [[Perception]]