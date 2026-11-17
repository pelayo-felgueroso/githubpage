## Explanation

The Median Filter is an image smoothing technique used mainly to reduce noise while preserving edges.

For each pixel, the filter looks at a neighbourhood and replaces the central pixel with the median value of all the pixels in that neighbourhood.

For example, with a 3 × 3 filter, the algorithm takes the nine pixel values, sorts them and selects the value in the middle.

Unlike an averaging filter, the median filter does not calculate the mean of the neighbouring pixels. This makes it particularly effective against salt-and-pepper noise, where individual pixels have very high or very low intensity values.

It is commonly used when isolated noisy pixels need to be removed without blurring object boundaries as much as a simple averaging filter would. However, large filter sizes can still remove fine details.

## Resources

_Learn more from external sources._

- [OpenCV – Smoothing Images](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
    
- [OpenCV – Image Filtering Functions](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html)
    
- [Computerphile – How Blurs & Filters Work](https://www.youtube.com/watch?v=R3C2giDfmO8)
## Related concepts

_Explore the knowledge network._

- [[Image Filtering]]
    
- [[Image Smoothing]]
    
- [[Noise]]
    
- [[Gaussian Blur]]
    
- [[Bilateral Filter]]