## Explanation

Stereo Vision is a computer vision technique used to estimate depth by comparing images captured from two cameras positioned at different locations.

Because the cameras observe the scene from slightly different viewpoints, the same point appears at different positions in the two images. This difference is called disparity.

By calculating the disparity and knowing the distance between the cameras, it is possible to estimate the distance of objects from the cameras.

For a rectified stereo camera system, depth can be calculated as:

$$  
Z = \frac{fB}{d}  
$$

Where:

- $Z$ is the distance to the point.
    
- $f$ is the focal length.
    
- $B$ is the distance between the two cameras, known as the baseline.
    
- $d$ is the disparity.
    

The basic idea is that points closer to the cameras produce larger disparities, while points further away produce smaller disparities.

Stereo vision requires the two cameras to be calibrated and their images aligned, a process known as stereo rectification. It can be difficult to estimate depth in areas with little texture, repetitive patterns or poor lighting.

Stereo vision is used in 3D reconstruction, autonomous driving and robotics. It is also one of the technologies used by some [[RGB-D Camera]]s.

## Resources

_Learn more from external sources._

- [OpenCV – Depth Map from Stereo Images](https://docs.opencv.org/4.x/dd/d53/tutorial_py_depthmap.html)
    
- [OpenCV – Stereo Calibration and 3D Reconstruction](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html)
    

## Related concepts

_Explore the knowledge network._

- [[Computer Vision]]
    
- [[Cameras]]
    
- [[Camera Calibration]]
    
- [[Focal Length]]
    
- [[Depth Estimation]]
    
- [[Point Clouds]]
    
- [[RGB-D Camera]]