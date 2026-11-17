## Explanation

Camera calibration is the process of estimating the parameters that describe how a camera captures the world.

These parameters are usually divided into two groups:

**Intrinsic parameters** describe the camera itself. They include focal length, principal point and lens distortion coefficients.

**Extrinsic parameters** describe the position and orientation of the camera relative to another coordinate frame.

A common way to estimate intrinsic parameters is to use a checkerboard. The camera captures several images of the board from different positions and orientations. Since the geometry of the checkerboard is known, its detected corners can be used to estimate the camera parameters.

With OpenCV, this can be done using functions such as:

- `cv2.findChessboardCorners()`
- `cv2.calibrateCamera()`
- `cv2.undistort()`

In robotics, we often need to know where the camera is relative to the robot. This is where hand-eye calibration comes in.

There are two common configurations:

- **Eye-in-hand:** the camera is mounted on the robot's wrist or end effector.
- **Eye-to-hand:** the camera is fixed in the environment, independently of the robot.

Hand-eye calibration estimates the transformation between the camera and the robot. A common mathematical formulation is AX = XB.

A small calibration error can produce a significant positioning error when the robot tries to grasp an object. Detecting an object correctly is not enough if its position cannot be accurately converted into robot coordinates.
## Resources

_Learn more from external sources._

- [OpenCV – Camera Calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
    
- [OpenCV – Camera Calibration and 3D Reconstruction](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html)

## Related concepts

_Explore the knowledge network._

- [[Cameras]]
    
- [[Pinhole Camera Model]]
    
- [[Focal Length]]
    
- [[Computer Vision]]