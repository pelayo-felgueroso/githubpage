## Explanation

Robots use coordinate frames to describe the position and orientation of their different parts. For example, a robot arm, its end effector and a camera can each have their own coordinate frame.

[[Coordinate Transformations]] allow us to express the position of one frame relative to another. This is important when combining information from different parts of a robot or from external sensors.

For example, if a camera detects an object, we need to transform its position from the camera frame to the robot frame before the robot can move towards it.

## Resources

_Learn more from external sources._

## Related concepts

_Explore the knowledge network._

- [[Kinematics]]
    
- [[Forward Kinematics]]
    
- [[Inverse Kinematics]]
    
- [[Computer Vision]]
    
- [[Camera Calibration]]