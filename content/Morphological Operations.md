## Explanation

**Morphological Operations** are image processing techniques used to modify the shape and structure of objects in an image.

They are based on the shape of a small element called a [[Structuring Element]], which is moved across the image to perform operations on its pixels.

The two basic morphological operations are:

- [[Erosion]]: Shrinks the foreground objects.
    
- [[Dilation]]: Expands the foreground objects.
    

These operations can also be combined to create more advanced techniques:

- [[Opening]]: Erosion followed by dilation. Useful for removing small objects and noise.
    
- [[Closing]]: Dilation followed by erosion. Useful for filling small holes and gaps.

## Resources

_Learn more from external sources._

- [ Udacity – Basic Morphological Algorithms](https://www.youtube.com/watch?v=SfHJlinkPK8)
    
- [Morphological Filtering – scikit-image](https://scikit-image.org/docs/stable/auto_examples/applications/plot_morphology.html)
    
- [ Udacity – Dilation and Erosion](https://www.youtube.com/watch?v=uUweXBmm978)

## Related concepts

_Explore the knowledge network._

- [[Image Processing]]
    
- [[Computer Vision]]
    
- [[Binary Images]]