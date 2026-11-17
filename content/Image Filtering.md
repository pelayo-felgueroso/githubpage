## Explanation

Image filtering is a technique used to modify an image by processing its pixel values and their neighbours.

Filters can be divided into two main groups: [[Linear Filters]] and [[Non-Linear Filters]].

Linear filters calculate each output pixel using a weighted combination of its neighbouring pixels. A common way to do this is with a kernel, which is a small matrix that moves across the image. This operation is known as convolution. [[Gaussian Blur]] and the [[Sobel Operator]] are examples of linear filters.

Non-linear filters use other methods to calculate the output pixel, rather than a simple weighted sum. For example, the [[Median Filter]] selects the middle value in a neighbourhood, while the [[Bilateral Filter]] considers both the spatial distance and intensity differences between pixels.

Filtering is commonly used as a preprocessing step in computer vision. Some filters reduce noise, while others enhance details or detect changes in image intensity. The choice depends on the type of noise, the image characteristics and the information that needs to be preserved.

## Resources

_Learn more from external sources._

- [OpenCV – Smoothing Images](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
    
- [OpenCV – Image Filtering Functions](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html)
    
- [Computerphile – How Blurs & Filters Work](https://www.youtube.com/watch?v=C_zFhWdM4ic)
## Related concepts

_Explore the knowledge network._

- [[Image Processing]]
    
- [[Linear Filters]]
    
- [[Non-Linear Filters]]
    
- [[Image Smoothing]]
    
- [[Gaussian Blur]]
    
- [[Median Filter]]
    
- [[Bilateral Filter]]
    
- [[Edge Detection]]
    
- [[Noise]]