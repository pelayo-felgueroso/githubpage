## Explanation

The Bilateral Filter is a non-linear image smoothing technique that reduces noise while trying to preserve edges.

Unlike a simple [[Gaussian Blur]], which considers only the spatial distance between pixels, the Bilateral Filter considers two things: how close the pixels are to each other and how similar their intensity values are.

Nearby pixels with similar intensity values have more influence on the result, while pixels with very different intensity values have less influence. This helps prevent smoothing across strong edges.

The filter is useful when reducing noise without losing important details, although it can be computationally more expensive than simpler filters.

## Resources

_Learn more from external sources._

- [OpenCV – Smoothing Images](https://docs.opencv.org/4.x/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html)
    
- [Computerphile – How Blurs & Filters Work](https://www.youtube.com/watch?v=R3C2giDfmO8)
    
- [First Principles of Computer Vision – Non-Linear Image Filters](https://www.youtube.com/watch?v=7FP7ndMEfsc)
## Related concepts

_Explore the knowledge network._

- [[Image Filtering]]
    
- [[Image Smoothing]]
    
- [[Gaussian Blur]]
    
- [[Median Filter]]
    
- [[Edge Detection]]