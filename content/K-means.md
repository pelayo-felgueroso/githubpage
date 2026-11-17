## Explanation

K-means is a clustering algorithm that groups similar data points together. It is called unsupervised learning because it does not need predefined labels. Instead, we tell it how many groups we want to find, and it tries to organise the data into those groups.

The algorithm works by choosing K initial points, called centroids, which represent the centre of each group. Each data point is assigned to its nearest centroid. The centroids are then moved to the average position of the points assigned to them. This process is repeated until the groups stop changing significantly.

For example, imagine a collection of points with different colours. If we choose K = 3, K-means will try to divide them into three groups of similar colours.

In image processing, we can use the same idea to group pixels according to their colour. Each pixel is represented by its RGB values, and K-means groups pixels with similar values together. This can be used for [[Image Segmentation]], as well as reducing the number of colours in an image.

However, K-means only looks at the features we give it. If two different objects have similar colours, they may end up in the same group. It does not understand what the objects are or where their boundaries should be.

## Resources

_Learn more from external sources._

- [Computerphile – K-means & Image Segmentation](https://www.youtube.com/watch?v=yR7k19YBqiw)
## Related concepts

_Explore the knowledge network._

- [[Image Segmentation]]
    
- [[Machine Learning]]
    
- [[Pixels]]
    
- [[Image Processing]]