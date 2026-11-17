## Explanation

Image classification is a computer vision task where a model assigns one or more labels to an image based on its visual content.

For example, a model can classify an image as containing a cat, a car or a person. In industrial applications, it can be used to identify different product types or determine whether a manufactured part belongs to a certain category.

Traditional approaches used manually designed image features combined with machine learning algorithms. Modern approaches mainly use [[Deep Learning]], especially [[Convolutional Neural Network]] architectures, which learn useful visual features directly from training images.

A classification model is trained using images associated with known labels. During training, it learns to recognise patterns that distinguish the different classes. Once trained, it can predict the class of images it has not seen before.

Image classification usually assigns a label to the whole image. This is different from [[Object Detection]], which also identifies where objects are located, and [[Image Segmentation]], which assigns a class to individual pixels.

## Resources

_Learn more from external sources._

- [PyTorch – Transfer Learning for Computer Vision](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
    
- [Hugging Face – Image Classification](https://huggingface.co/docs/transformers/tasks/image_classification)


## Related concepts

_Explore the knowledge network._

- [[Computer Vision]]
    
- [[Machine Learning]]
    
- [[Deep Learning]]
    
- [[Neural Networks]]
    
- [[Convolutional Neural Network]]
    
- [[Object Detection]]
    
- [[Image Segmentation]]