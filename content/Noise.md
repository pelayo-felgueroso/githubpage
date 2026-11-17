## Explanation

Noise refers to unwanted variations or random disturbances in a signal or measurement. In images, it appears as changes in pixel intensity that do not correspond to the actual scene.

Noise can come from different sources, such as camera sensors, electronic components, lighting conditions, image acquisition and data transmission.

Common types of image noise include:

- Gaussian noise, which follows a Gaussian probability distribution and produces random intensity variations across the image.
    
- Salt-and-pepper noise, which appears as isolated bright and dark pixels.
    
- Poisson noise, which is related to the statistical nature of photon detection and is particularly relevant in low-light imaging.
    

Noise can make it harder to identify objects, detect edges and perform accurate measurements. Its effect depends on the type and amount of noise, as well as the characteristics of the image.

Different [[Image Filtering]] and [[Image Smoothing]] techniques can be used to reduce noise. However, removing noise is not always straightforward because the filter can also remove useful details. The goal is to find a balance between noise reduction and preserving the information in the image.

## Resources

_Learn more from external sources._

- [OpenCV – Smoothing Images](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
    
- [scikit-image – Denoising](https://scikit-image.org/docs/stable/auto_examples/filters/plot_denoise.html)

## Related concepts

_Explore the knowledge network._

- [[Image Processing]]
    
- [[Image Filtering]]
    
- [[Image Smoothing]]
    
- [[Gaussian Blur]]
    
- [[Median Filter]]
    
- [[Bilateral Filter]]