## Explanation

The Hough Transform is an image processing technique used to detect geometric shapes in an image, especially lines and circles.

It works by transforming information from the image into a parameter space. Instead of trying to identify a complete line directly, the algorithm considers which possible lines could pass through each detected image point.

Points that belong to the same line contribute to the same region of the parameter space. When enough points support a particular line, the algorithm identifies it as a possible detection.

The Hough Transform is often applied after [[Edge Detection]], because edges provide useful information about the boundaries of objects. It can be used to detect lines in road images, circles in industrial components or other regular shapes.

One limitation is that the method can be sensitive to noise and parameter selection. It can also detect unwanted lines when the image contains many edges.

## Resources

_Learn more from external sources._

- [OpenCV – Hough Line Transform](https://docs.opencv.org/4.x/d6/d10/tutorial_py_houghlines.html)
    
- [OpenCV – Hough Circle Transform](https://docs.opencv.org/4.x/da/d53/tutorial_py_houghcircles.html)
    
- [First Principles of Computer Vision - Hough Transform | Boundary Detection](https://www.youtube.com/watch?v=XRBc_xkZREg&t=117s)

## Related concepts

- [[Image Processing]]
    
- [[Edge Detection]]
    
- [[Canny Edge Detector]]
    
- [[Gradient Calculation]]