## Explanation

Gradient calculation is the process of measuring how quickly the intensity of an image changes from one pixel to its neighbours. It helps identify areas where the image changes significantly, which often correspond to object boundaries or edges.

An image can be analysed in the horizontal and vertical directions. The horizontal gradient detects changes from left to right, while the vertical gradient detects changes from top to bottom. Combining both gives information about the strength and direction of the intensity change.

Gradient calculation is an important part of many image processing techniques. For example, the [[Sobel Operator]] estimates gradients using convolution kernels, while the [[Canny Edge Detector]] uses gradient information to identify edges.

It is also used in other computer vision tasks, such as feature detection, image segmentation and optical flow.

## Resources

_Learn more from external sources._

- [OpenCV – Image Gradients](https://docs.opencv.org/4.x/d5/d0f/tutorial_py_gradients.html)
    
- [OpenCV – Sobel Derivatives](https://docs.opencv.org/4.x/d2/d2c/tutorial_sobel_derivatives.html)
## Related concepts

_Explore the knowledge network._

- [[Image Processing]]
    
- [[Edge Detection]]
    
- [[Sobel Operator]]
    
- [[Laplacian Operator]]
    
- [[Canny Edge Detector]]