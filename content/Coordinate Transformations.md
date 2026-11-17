## Explanation

Coordinate transformations are used to describe the position and orientation of an object relative to different coordinate frames.

In robotics and computer vision, different coordinate frames are used for the robot base, its joints, the end effector, cameras and objects in the environment. A transformation allows us to express a position defined in one frame using another frame.

For example, a camera can detect an object in its own coordinate frame, but the robot needs to know the object's position relative to its base to reach it. Coordinate transformations make this conversion possible.

They are usually represented using transformation matrices, which combine rotation and translation.

## Resources

_Learn more from external sources._

- [Robotics, Control and Machine Learning – Coordinate Frames](https://www.youtube.com/watch?v=Ygb8jzFVA-w)
## Related concepts

- [[Coordinate Frames]]
    
- [[Camera Calibration]]
    
- [[Forward Kinematics]]
    
- [[Inverse Kinematics]]
    
- [[Robotics]]