## Explanation

U-Net is a convolutional neural network architecture originally developed for biomedical image segmentation.

Its structure consists of two main parts: an encoder and a decoder. The encoder progressively reduces the spatial resolution of the image while extracting increasingly complex features. The decoder then uses these features to reconstruct a segmentation map with the original image resolution.

A key feature of U-Net is the use of skip connections, which transfer information from the encoder to corresponding layers in the decoder. This helps preserve spatial details that could otherwise be lost during downsampling.

U-Net is particularly useful when the output needs to identify the exact location of objects or regions in an image, rather than simply assigning a label to the entire image.

It is widely used for medical image segmentation and has also been adapted for other image processing tasks, including image restoration and denoising.

## Resources

_Learn more from external sources._

- [U-Net – Original Paper](https://arxiv.org/abs/1505.04597)
    
- [Milesial – PyTorch U-Net GitHub Repository](https://github.com/milesial/Pytorch-UNet)
    
- [PyTorch – Semantic Segmentation Models](https://docs.pytorch.org/vision/stable/models.html#semantic-segmentation)
    

## Related concepts

_Explore the knowledge network._

- [[Deep Learning]]
    
- [[Neural Networks]]
    
- [[Convolutional Neural Network]]
    
- [[Image Segmentation]]
    
- [[Image Classification]]
    
- [[Image Processing]]