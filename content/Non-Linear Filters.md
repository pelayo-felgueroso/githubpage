## Explanation

Non-linear filters modify pixel values using operations that cannot be expressed as a simple weighted sum of the neighbouring pixels.

Unlike [[Linear Filters]], they do not necessarily use convolution. Instead, they can use operations such as selecting the median value or comparing the intensity values of neighbouring pixels.

For example, the [[Median Filter]] replaces each pixel with the median value of its neighbourhood. This makes it effective at removing salt-and-pepper noise. The [[Bilateral Filter]] considers both spatial distance and intensity differences, allowing it to smooth an image while preserving edges.

Non-linear filters are useful when a simple average would remove important image details or when the noise has specific characteristics. Their main limitation is that they can be more computationally expensive, depending on the operation.

## Resources

_Learn more from external sources._

- [First Principles of Computer Vision – Non-Linear Image Filters](https://www.youtube.com/watch?v=7FP7ndMEfsc)

## Related concepts

_Explore the knowledge network._

- [[Image Filtering]]
    
- [[Linear Filters]]
    
- [[Median Filter]]
    
- [[Bilateral Filter]]
    
- [[Morphological Operations]]
    
- [[Noise]]
    
- [[Image Smoothing]]