## Explanation

Otsu's Method is an automatic thresholding technique used to separate the foreground from the background in a grayscale image.

Instead of choosing a threshold manually, the algorithm analyses the image [[Histogram]] and finds a threshold that separates the pixels into two groups as effectively as possible.

It does this by selecting the threshold that maximises the difference between the two groups. In practice, this works well when the histogram contains two reasonably distinct intensity distributions, for example a dark background and a bright object.

The result is a [[Binary Images|binary image]] where pixels are classified according to the selected threshold.

Otsu's Method is useful because it provides an automatic way to choose a threshold without manually adjusting it for every image. However, it can be less effective when the foreground and background have similar intensity values, when the lighting is uneven or when the histogram does not contain two clearly separated groups.

## Resources

_Learn more from external sources._

- [OpenCV – Image Thresholding and Otsu's Binarization](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html)
    
- [Udacity – Thresholding](https://www.youtube.com/watch?v=6pX3II2eVs0)

## Related concepts

_Explore the knowledge network._

- [[Thresholding]]
    
- [[Binary Images]]
    
- [[Image Processing]]
    
- [[Image Segmentation]]
    
- [[Pixels]]