## Explanation

The Watershed Algorithm is an image segmentation technique used to separate objects that touch or overlap in an image.

It treats a grayscale image as a topographic surface, where pixel intensity represents height. Low-intensity regions can be seen as valleys, while high-intensity regions represent hills.

The algorithm starts from selected markers and expands regions until different regions meet. The boundaries between them form the segmentation lines, similar to the boundaries between water catchment basins.

In practice, the algorithm is often combined with thresholding and morphological operations to prepare the image and identify suitable markers. These markers help the algorithm distinguish between different objects and the background.

It is particularly useful when several objects are connected or touching, making it difficult to separate them using simple thresholding alone.

One limitation is that the result depends strongly on the quality of the markers. Poor markers can lead to over-segmentation, where one object is incorrectly divided into several regions.

## Resources

_Learn more from external sources._

- [OpenCV – Image Segmentation with Watershed Algorithm](https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html)
    
- [scikit-image – Watershed Segmentation](https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_watershed.html)

## Related concepts

_Explore the knowledge network._

- [[Image Processing]]
    
- [[Image Segmentation]]
    
- [[Thresholding]]
    
- [[Binary Images]]
    
- [[Morphological Operations]]
    
- [[Pixels]]