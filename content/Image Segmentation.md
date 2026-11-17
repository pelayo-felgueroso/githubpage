## Explanation

Image segmentation is the process of dividing an image into regions or assigning a label to each pixel. The goal is to separate objects or areas that we want to analyse from the rest of the image.

There are different approaches depending on the image and the result we want. [[Thresholding]] classifies pixels according to their intensity, which works well when there is a clear difference between an object and its background. [[Otsu's Method]] automatically finds a suitable threshold based on the image histogram.

Another approach is clustering. [[K-means]] groups pixels according to similarities in their features, such as colour or intensity. This can be used to separate regions with similar characteristics without manually defining a threshold.

The [[Watershed Algorithm]] uses a different approach. It treats an image as a topographic surface and uses its structure to separate regions, making it particularly useful for distinguishing objects that touch each other.

For more complex images, segmentation can also be performed using [[Deep Learning]] models. Architectures such as [[U-Net]] are widely used to classify pixels, particularly in medical and scientific imaging.

There are also different types of segmentation depending on what we want to identify. [[Semantic Segmentation]] assigns a class to each pixel, while [[Instance Segmentation]] also distinguishes between individual objects belonging to the same class.

In robotics, segmentation is useful when a robot needs to isolate an object from its surroundings. For example, separating a bottle from a shelf makes it easier to combine the image with depth information and estimate the object's 3D position.

## Resources

_Learn more from external sources._

- [Computerphile - K-means & Image Segmentation](https://www.youtube.com/watch?v=yR7k19YBqiw)

## Related concepts

_Explore the knowledge network._

- [[Computer Vision]]
    
- [[Image Processing]]
    
- [[Edge Detection]]
    
- [[Object Detection]]
    
- [[Deep Learning]]
    
- [[Thresholding]]
    
- [[Watershed Algorithm]]