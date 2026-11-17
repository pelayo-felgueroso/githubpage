## Explanation

Robot Simulation is the process of creating a virtual representation of a robot and its environment to test and develop robotic systems without always needing physical hardware.

A simulator can reproduce the robot's mechanical structure, joint movements, sensors, objects and interactions with the environment. Depending on the simulator, it can also model physical properties such as gravity, friction, collisions and actuator behaviour.

Simulation is useful for testing algorithms, validating robot movements, developing controllers and generating training data. It also makes it possible to test situations that could be difficult, expensive or dangerous to reproduce with a real robot.

Common robotics simulators include Gazebo, NVIDIA Isaac Sim and MuJoCo. They can also be integrated with frameworks such as [[ROS 2]].

Although simulation is useful during development, a simulated environment is never a perfect representation of reality. Differences in physics, sensors and object behaviour can affect performance when a system is transferred to a real robot. This is known as the [[Sim-to-Real]] problem.

## Resources

_Learn more from external sources._

- [Gazebo – Documentation](https://gazebosim.org/docs/)
    
- [NVIDIA Isaac Sim – Documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)
    
- [MuJoCo – Documentation](https://mujoco.readthedocs.io/)

## Related concepts

_Explore the knowledge network._

- [[Robotics]]
    
- [[ROS 2]]
    
- [[Motion Planning]]
    
- [[Robot Learning]]
    
- [[Sim-to-Real]]
    
- [[Sensors]]