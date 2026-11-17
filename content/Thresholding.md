## Explanation

Thresholding is an image processing technique used to separate pixels based on their intensity values.

A threshold is selected and each pixel is compared against it. Depending on the result, the pixel is assigned to one of two or more output values. A common application is converting a grayscale image into a [[Binary Images|binary image]], where pixels become either black or white.

There are different types of thresholding. Global thresholding applies the same threshold to the entire image, while adaptive thresholding calculates different thresholds for local regions. This can be useful when the lighting is uneven.

The threshold can also be selected automatically. For example, [[Otsu's Method]] analyses the image histogram to find a suitable threshold without requiring the user to choose it manually.

Thresholding is commonly used for object segmentation, industrial inspection and image analysis. However, it works best when the foreground and background have sufficiently different intensity values. Changes in illumination, shadows or noise can make the separation more difficult.

## Resources

_Learn more from external sources._

- [OpenCV – Image Thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html)
    
- [Udacity – Thresholding](https://www.youtube.com/watch?v=6pX3II2eVs0)
## Related concepts

_Explore the knowledge network._

- [[Image Processing]]
    
- [[Binary Images]]
    
- [[Otsu's Method]]
    
- [[Image Segmentation]]
    
- [[Pixels]]