## Explanation

Gaussian Blur is an image filtering technique used to reduce noise and small variations in intensity. It works by convolving an image with a Gaussian kernel, which assigns higher weights to pixels near the centre and progressively lower weights to pixels farther away.

Unlike a simple averaging filter, Gaussian Blur gives more importance to nearby pixels, producing a smoother result while reducing abrupt intensity changes. The amount of blur depends mainly on the kernel size and the standard deviation ((\sigma)) of the Gaussian function.

It is commonly used as a preprocessing step before edge detection, thresholding and image segmentation. For example, applying Gaussian Blur before the Canny edge detector helps reduce false edges caused by image noise.

The main drawback is that it also removes fine details and can make object boundaries less precise if the filtering is too strong.

## Resources

[OpenCV – Smoothing Images](https://docs.opencv.org/4.x/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html)

## Related concepts

_Explore the knowledge network._

- [[Median Filter]]
    
- [[Bilateral Filter]]
    
- [[]]