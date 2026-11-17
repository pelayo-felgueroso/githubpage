## Explanation

Robot joints connect the different links of a robot and allow relative movement between them.

The type of joint determines how two links can move with respect to each other. The most common types in robot arms are:

- Revolute joints, which allow rotation around an axis.
    
- Prismatic joints, which allow linear movement along an axis.
    

Each independent joint usually contributes one [[Degrees of Freedom (DOF)|degree of freedom]] to the robot. The arrangement of these joints determines how the robot can move and which positions it can reach.

Joints are often driven by [[Actuators]], such as electric motors. Their positions are used to describe the configuration of the robot and calculate the position of its end effector through [[Forward Kinematics]].

In real robots, joints also have physical limits, such as maximum rotation angles, speed and torque. These constraints need to be considered when planning and controlling robot movements.

## Resources

_Learn more from external sources._

- [Northwestern Robotics – Modern Robotics, Chapter 2.2: Degrees of Freedom of a Robot](https://www.youtube.com/watch?v=zI64DyaRUvQ)
    
- [MoveIt 2 – Robot Model and Robot State](https://moveit.picknik.ai/main/doc/examples/robot_model_and_robot_state/robot_model_and_robot_state_tutorial.html)

## Related concepts

_Explore the knowledge network._

- [[Robot Mechanics]]
    
- [[Robot Links]]
    
- [[Degrees of Freedom (DOF)]]
    
- [[Actuators]]
    
- [[Electric Motors]]
    
- [[Kinematics]]
    
- [[Forward Kinematics]]