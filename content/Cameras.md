## Explanation

A camera captures light from the environment and converts it into a digital image. What we get is a 2D representation of a 3D scene, made up of pixels.

The way this projection happens is usually described using the [[Pinhole Camera Model]]. It explains how a 3D point in the real world ends up at a particular pixel in an image. Real cameras are more complicated because lenses introduce effects such as [[Lens Distortion]].

There are different types of cameras depending on what information we need. A standard [[RGB camera]] captures colour, while [[Stereo Vision]] uses two cameras to estimate depth. [[RGB-D Camera]] provide both colour and depth information, which is particularly useful in robotics.

Camera characteristics such as [[Resolution]], [[Focal Length]], [[Field of View]] and [[Frame Rate]] also affect the quality of the captured images and what we can do with them. 

In robotic applications, the camera is often the first step in the perception pipeline. The images it captures are processed to detect objects, estimate their position and eventually allow the robot to interact with them.

## Resources

_Learn more from external sources._

- [Computerphile – Capturing Digital Images (The Bayer Filter)](https://www.youtube.com/watch?v=LWxu4rkZBLw)
    
- [Computerphile – Digital Images](https://www.youtube.com/watch?v=06OHflWNCOE) 
    
- [Camera Calibration – OpenCV](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
## Related concepts

- [[Computer Vision]]
    
- [[Camera Calibration]]
    
- [[Depth Estimation]]
    
- [[Image Processing]]
    
- [[Point Clouds]]

