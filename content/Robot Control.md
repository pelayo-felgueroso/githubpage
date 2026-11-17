## Explanation

Robot control is about making a robot move and behave as intended. It uses commands and feedback to control the position, velocity or force of its joints and [[end effector]].

A controller compares the robot's current state with the desired state and calculates the commands needed to reduce the difference. This can be done using open-loop control, where commands are sent without checking the result, or closed-loop control, where sensor measurements are used to continuously adjust the robot's behaviour.

Different control methods are used depending on the task. For example, position control moves joints to specific angles, velocity control regulates how fast they move, and force control regulates the forces applied during interaction with the environment.

Robot control works closely with [[Kinematics]], [[Motion Planning]] and [[Sensors]]. Motion planning determines how the robot should move, while the controller makes that movement happen on the physical system.

One of the most common control methods is [[PID Control]], which adjusts the commands sent to the robot based on the difference between the desired and actual state. It combines proportional, integral and derivative terms to reduce this error over time.
## Resources

_Learn more from external sources._

- [Mike Likes Robots – Building a ros2_control System | ROS2 Control with the JetBot Part 2](https://www.youtube.com/watch?v=2JJApj-PNVk)
## Related concepts

_Explore the knowledge network._

- [[Actuators]]
    
- [[Robot Joints]]
    
- [[Sensors]]
    
- [[Kinematics]]
    
- [[Motion Planning]]