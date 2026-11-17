## Explanation

Lens distortion is an optical effect that causes straight lines in the real world to appear curved in an image. It is produced by the geometry and properties of the camera lens.

There are two common types of lens distortion:

- Radial distortion causes straight lines to appear curved. Barrel distortion makes lines curve outwards, while pincushion distortion makes them curve inwards.
    
- Tangential distortion occurs when the lens and image sensor are not perfectly aligned.
    

Lens distortion is particularly important in computer vision and machine vision because it affects the position of points in an image. This can lead to errors when measuring dimensions, estimating object positions or reconstructing a 3D scene.

The distortion can be modelled using camera parameters and corrected through [[Camera Calibration]]. This process usually involves capturing images of a known calibration pattern from different positions and estimating the distortion coefficients.

## Resources

_Learn more from external sources._

- [OpenCV – Camera Calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
    
- [OpenCV – Camera Calibration and 3D Reconstruction](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html)

## Related concepts

_Explore the knowledge network._

- [[Cameras]]
    
- [[Camera Calibration]]
    
- [[Pinhole Camera Model]]
    
- [[Focal Length]]
    
- [[Computer Vision]]