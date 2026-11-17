## Explanation

ROS 2 (Robot Operating System 2) is an open-source framework used to develop robot software. It provides tools and communication mechanisms that allow different parts of a robotic system to work together.

A ROS 2 application is usually organised into nodes, which are individual processes responsible for specific tasks. Nodes communicate through topics, services and actions.

Topics are used to continuously exchange data, such as camera images or sensor measurements. Services provide a request-and-response mechanism for operations that finish relatively quickly. Actions are used for longer-running tasks that may provide feedback and can be cancelled.

ROS 2 also provides tools for handling coordinate frames, robot descriptions, hardware interfaces, simulation and visualisation. Other frameworks, such as MoveIt 2, build on ROS 2 to provide capabilities for robotic manipulation and motion planning.

For example, a camera node can publish images, a perception node can process them and identify an object, and a motion planning system can calculate how the robot should move.

ROS 2 is widely used in research and industry to build modular robotic systems. It does not control every aspect of a robot automatically; developers still need to integrate the software with the robot's hardware and configure the communication and control systems.

## Resources

_Learn more from external sources._

- [Mike Likes Robots – Getting Started with ROS 2](https://www.youtube.com/watch?v=8aoFndU7jos)
    
- [ROS 2 – Official Documentation](https://docs.ros.org/en/rolling/)
    
- [ROS 2 – Tutorials](https://docs.ros.org/en/rolling/Tutorials.html)
## Related concepts

_Explore the knowledge network._

- [[Robotics]]
    
- [[Robot Simulation]]
    
- [[Motion Planning]]
    
- [[Sensors]]
    
- [[Perception]]
    
- [[Robot Learning]]