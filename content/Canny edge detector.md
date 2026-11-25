## Explanation

The Canny Edge Detector is an algorithm used to detect edges in an image. It identifies areas where the intensity changes significantly, which often correspond to the boundaries of objects.

The algorithm follows five main steps:

1. **Gaussian smoothing:** Applies a Gaussian filter to reduce noise and prevent false edge detections.
    
2. **Gradient calculation:** Computes the intensity gradients using operators such as Sobel, determining the magnitude and direction of intensity changes.
    
3. **Non-maximum suppression:** Thins the detected edges by keeping only local maxima along the gradient direction, removing weaker responses that do not correspond to the centre of an edge.
    
4. **Double thresholding:** Classifies pixels as strong, weak or non-edges based on two intensity thresholds.
    
5. **Hysteresis thresholding:** Determines which weak edges should be retained by checking their connectivity to strong edges. Weak edges connected to strong edges are preserved, while isolated weak edges are discarded.
    

The result is usually a binary image where detected edges appear as white lines on a black background.

## Resources

_Learn more from external sources._

- [OpenCV – Canny Edge Detection](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)
    
- [Computerphile – Canny Edge Detection](https://www.youtube.com/watch?v=sRFM5IEqR2w&t=343s)
    
## Related concepts

_Explore the knowledge network._

- [[Edge Detection]]
    
- [[Image Processing]]
    
- [[Gaussian Blur]]
    
- [[Sobel Operator]]
    
- [[Binary Images]]