## Explanation

Object detection is about finding objects in an image and determining where they are. Unlike [[Image Classification]], which tells us what an image contains, object detection also gives us the location of each object, usually through a bounding box.

Most detection models predict a class, a bounding box and a confidence score. The confidence score indicates how confident the model is about its prediction, although it doesn't necessarily represent the true probability that the detection is correct.

For example:

```
Class: bottle
Confidence: 0.94
Bounding box: [450, 200, 600, 450]
```

There are several approaches to object detection. Older and traditional methods include sliding windows and feature-based detectors. Modern systems mainly use [[Deep Learning]]. Models such as [[YOLO]] are designed for fast detection.

Detection is often combined with [[Image Segmentation]] when a bounding box isn't precise enough, or with [[Object Tracking]] when we need to follow an object across multiple frames.

In robotics, detecting an object is only the beginning. A bounding box tells us where it appears in the image, but not necessarily its actual 3D position or orientation. For manipulation, this information usually needs to be combined with depth data and [[Pose Estimation]].

## Resources

_Learn more from external sources._

## Related concepts

_Explore the knowledge network._

- [[]]
    
- [[]]
    
- [[]]