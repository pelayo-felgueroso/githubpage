## Explanation

Edge detection is an image processing technique used to find boundaries between different regions in an image. These boundaries usually correspond to changes in brightness, colour or texture, and often indicate where one object or region ends and another begins.

The basic idea is to look for strong changes in pixel intensity. This is usually done by calculating image gradients, which describe how quickly the intensity changes in horizontal and vertical directions.

There are several ways to do this. The [[Sobel Operator]] calculates image gradients using small convolution kernels, while the [[Laplacian Operator]] looks at second-order intensity changes. The [[Canny Edge Detector]] combines several steps, including noise reduction, gradient calculation and edge tracking, to produce cleaner and more connected edges.

Before detecting edges, it is often useful to apply [[Gaussian Blur]] to reduce noise. Otherwise, small intensity variations can produce unwanted edges.

Edge detection is useful for tasks such as contour extraction, shape analysis, object recognition and measurement. It can also be combined with methods such as the [[Hough Transform]] to detect geometric structures like lines and circles.

Although deep learning has replaced some traditional approaches in complex applications, these techniques are still useful when the image conditions are controlled or when we need a relatively simple and interpretable solution.


## Resources

_Learn more from external sources._

- [Computerphile – Finding the Edges (Sobel Operator)](https://www.youtube.com/watch?v=uihBwtPIBxM)
## Related concepts

_Explore the knowledge network._

- [[Computer Vision]]
    
- [[Image Processing]]
    
- [[Image Segmentation]]
    
- [[Object Detection]]
    
- [[Image Filtering]]
    
- [[Canny Edge Detector]]
