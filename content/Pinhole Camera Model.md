## Explanation

The Pinhole Camera Model is a simplified mathematical representation of how a camera projects points from three-dimensional space onto a two-dimensional image plane.

It assumes that light travels in straight lines through a small opening, called the pinhole, and reaches the image plane. This creates a perspective projection where objects appear smaller as their distance from the camera increases.

The projection can be described using:

$$  
u = f_x\frac{X}{Z} + c_x  
$$

$$  
v = f_y\frac{Y}{Z} + c_y  
$$

Where:

- $(X,Y,Z)$ are the coordinates of a 3D point in the camera frame.
    
- $(u,v)$ are the corresponding pixel coordinates.
    
- $f_x$ and $f_y$ are the focal lengths expressed in pixels.
    
- $c_x$ and $c_y$ are the coordinates of the principal point.
    

The model is a simplified representation of a real camera, but it is fundamental to [[Computer Vision]]. It is used to understand how 3D points appear in an image and forms the basis of camera calibration, stereo vision and 3D reconstruction.

Real cameras also introduce optical effects such as [[Lens Distortion]], which need to be modelled separately.

## Resources

_Learn more from external sources._

- [MIT – Vision Book: Camera Models](https://visionbook.mit.edu/imaging.html)

## Related concepts

_Explore the knowledge network._

- [[Cameras]]
    
- [[Camera Calibration]]
    
- [[Lens Distortion]]
    
- [[Focal Length]]
    
- [[Coordinate Frames]]
    
- [[Stereo Vision]]