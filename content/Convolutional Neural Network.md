## Explanation

A Convolutional Neural Network (CNN) is a type of [[Neural Networks|neural network]] designed to process data with a grid-like structure, such as images.

Instead of connecting every neuron to every input pixel, CNNs use convolutional layers that apply small filters, also called kernels, across the image. These filters learn to detect visual patterns such as edges, textures and shapes.

As the information passes through multiple layers, the network can learn increasingly complex features. Early layers often detect simple patterns, while deeper layers can recognise more complex structures and objects.

CNNs commonly combine convolutional layers with activation functions, pooling operations and fully connected layers. Convolutional layers extract features, pooling can reduce the spatial size of the feature maps, and fully connected layers can use the extracted information to make a final prediction.

CNNs are widely used in computer vision tasks such as [[Image Classification]], object detection and image segmentation. Architectures such as [[U-Net]] also use convolutional layers for pixel-level image segmentation.

## Resources

_Learn more from external sources._

- [PyTorch – Convolutional Neural Network Tutorial](https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)
    
- [3Blue1Brown – But What Is a Convolution?](https://www.3blue1brown.com/lessons/convolutions)

## Related concepts

- [[Neural Networks]]
    
- [[Deep Learning]]
    
- [[Machine Learning]]
    
- [[Image Classification]]
    
- [[Image Segmentation]]
    
- [[U-Net]]
    
- [[Transformer]]