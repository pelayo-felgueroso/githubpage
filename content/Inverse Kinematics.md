## Explanation

Inverse Kinematics is the process of calculating the joint positions required for a robot's end effector to reach a desired position and orientation.

Unlike [[Forward Kinematics]], where we know the joint positions and calculate the end effector pose, inverse kinematics starts with a target pose and tries to find the joint positions needed to reach it.

The general relationship can be expressed as:

$$  
\mathbf{q} = f^{-1}(\mathbf{x})  
$$

Where:

- $\mathbf{q}$ is the vector of joint positions.
    
- $\mathbf{x}$ is the desired position and orientation (pose) of the end effector.
    
- $f^{-1}$ represents the inverse kinematics solution.
    

Finding a solution is not always straightforward. A robot may have several joint configurations that reach the same target, or the target may be outside its reachable workspace. Joint limits and [[Robot Singularities]] can also affect the solution.

Inverse Kinematics is widely used in robotics when a robot needs to reach a specific position, follow a trajectory or manipulate an object.

## Resources

_Learn more from external sources._

- [PhysicsHigh– Kinematics - The basics](https://www.youtube.com/watch?v=198u1x8TBTo)
## Related concepts

_Explore the knowledge network._

- [[Kinematics]]
    
- [[Forward Kinematics]]
    
- [[Coordinate Frames]]
    
- [[Coordinate Transformations]]
    
- [[Jacobian Matrix]]
    
- [[Robot Singularities]]
    
- [[End Effector]]