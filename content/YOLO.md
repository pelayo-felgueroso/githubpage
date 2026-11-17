## Explanation

YOLO (You Only Look Once) is a family of Deep Learning models mainly used for [[Object Detection]]. It can identify objects in an image and estimate where they are, making it useful for applications that need to process images or video in real time.

Unlike traditional approaches that analyse different regions of an image separately, YOLO processes the entire image in a single pass through a neural network. It predicts which objects are present and where they are located at the same time. This is what makes it particularly fast.

For each detected object, YOLO provides three things: a class label, a bounding box and a confidence score. The class label identifies the object, the bounding box indicates its position in the image, and the confidence score indicates how confident the model is about its prediction.

For example, given an image containing several bottles and a person, YOLO can detect each object, identify its class and draw a bounding box around it. The same process can be repeated for every frame of a video, allowing objects to be detected in real time.

YOLO models are trained using labelled images containing the objects they need to recognise. Once trained, they can be used to detect objects in new images without having to define their positions manually.


## Resources

_Learn more from external sources._

- [Ultralytics – Object Detection with YOLO](https://docs.ultralytics.com/tasks/detect)
    
- [Original YOLO Paper – You Only Look Once: Unified, Real-Time Object Detection](https://openaccess.thecvf.com/content_cvpr_2016/html/Redmon_You_Only_Look_CVPR_2016_paper.html)
    
- [How YOLO Object Detection Works](https://www.youtube.com/watch?v=svn9-xV7wjk)

## Related concepts

_Explore the knowledge network._

- [[Object Detection]]
    
- [[Deep Learning]]
    
- [[Convolutional Neural Network]]
    
- [[Computer Vision]]
    
- [[Instance Segmentation]]
