## Explanation

Linear filters calculate each output pixel as a weighted sum of the surrounding pixel values. The weights are defined by a small matrix called a kernel, which moves across the image. This operation is known as convolution.

A filter is linear because it follows the principles of additivity and scaling: filtering a combination of images gives the same result as combining their individually filtered versions.

Different kernels produce different effects. For example, [[Gaussian Blur]] uses a kernel to smooth the image and reduce noise, while the [[Sobel Operator]] estimates intensity changes to detect edges.

Linear filters are widely used in image processing because they are relatively simple and efficient. However, smoothing filters can also blur edges, since they do not distinguish between pixels on opposite sides of an edge.

## Resources

_Learn more from external sources._

- [OpenCV – Smoothing Images](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
    
- [OpenCV – Image Gradients](https://docs.opencv.org/4.x/d5/d0f/tutorial_py_gradients.html)
    
- [First Principles of Computer Vision – Linear Image Filters](https://www.youtube.com/watch?v=-LD9MxBUFQo)
## Related concepts

_Explore the knowledge network._

- [[Image Filtering]]
    
- [[Non-Linear Filters]]
    
- [[Gaussian Blur]]
    
- [[Sobel Operator]]
    
- [[Image Smoothing]]
    
- [[Edge Detection]]