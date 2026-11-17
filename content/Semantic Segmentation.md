## Explanation

Semantic Segmentation is a type of image segmentation that assigns a class label to every pixel in an image. The goal is to identify which regions belong to each category, such as roads, buildings, people or vehicles.

All pixels belonging to the same class receive the same label, regardless of whether they belong to different objects. For example, if an image contains three cars, all three are classified as `car`. The segmentation does not distinguish between the individual vehicles.

This makes semantic segmentation useful when we want to understand the general contents of a scene rather than identify individual objects.

In robotics, it can help a robot distinguish between different parts of its environment, such as floors, shelves, walls and objects. It is also widely used in autonomous driving and medical image analysis.

Deep Learning models such as [[U-Net]] can perform semantic segmentation by learning to classify each pixel from training images.

## Resources

_Learn more from external sources._
[U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)
## Related concepts

_Explore the knowledge network._

- [[Image Segmentation]]
    
- [[Instance Segmentation]]
    
- [[Deep Learning]]
    
- [[Neural Networks]]
    
- [[U-Net]]
    
- [[Object Detection]]
    
- [[Computer Vision]]