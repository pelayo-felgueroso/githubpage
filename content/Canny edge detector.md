## Explanation

The Canny Edge Detector is an algorithm used to detect edges in an image. It identifies areas where the intensity changes significantly, which often correspond to the boundaries of objects.

The algorithm follows several steps. First, it applies Gaussian smoothing to reduce noise. Then, it calculates the intensity gradients and removes weaker responses that are not likely to belong to an edge. Finally, it uses two thresholds to decide which edges should be kept.

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