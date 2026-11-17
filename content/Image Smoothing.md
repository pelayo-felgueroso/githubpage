## Explanation

Image smoothing is an image processing technique used to reduce noise and small variations in pixel intensity. It is often applied before other processing steps to make an image easier to analyse.

Smoothing works by combining the intensity values of neighbouring pixels. This reduces sudden changes in intensity, but it can also remove fine details and make edges less sharp.

There are several ways to smooth an image. [[Gaussian Blur]] uses a weighted average, giving more importance to pixels close to the centre of the filter. The [[Median Filter]] replaces each pixel with the median value of its neighbourhood and is particularly useful for salt-and-pepper noise. The [[Bilateral Filter]] considers both spatial distance and intensity differences, helping to preserve edges while reducing noise.

The choice of method depends on the type of noise and how much detail needs to be preserved. For example, applying too much smoothing before edge detection can make small or weak edges disappear.

## Resources

_Learn more from external sources._

- [OpenCV – Smoothing Images](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
    
- [OpenCV – Image Filtering Functions](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html)
    
- [Computerphile – How Blurs & Filters Work](https://www.youtube.com/watch?v=C_zFhWdM4ic)
## Related concepts

_Explore the knowledge network._

- [[Image Processing]]
    
- [[Image Filtering]]
    
- [[Gaussian Blur]]
    
- [[Median Filter]]
    
- [[Bilateral Filter]]
    
- [[Noise]]
    
- [[Edge Detection]]