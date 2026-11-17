Imaging is the process of forming an image of the world by capturing light reflected from objects. Light from sources such as the sun or artificial lights hits surfaces and is reflected in different directions. The properties of the reflected light, such as its intensity and colour, depend on the material and orientation of the surface. A camera captures this light and uses it to create an image.

### Light and Surface Reflection

When light hits a surface, part of it is reflected. The way this happens depends on the surface properties and the direction of the incoming light. Two important types of reflection are diffuse and specular reflection.

**Diffuse reflection** occurs when light is scattered in many directions. A common approximation is the Lambertian model, where the brightness depends on the surface orientation relative to the light source, but not on the direction from which the surface is observed. The surface reflectance, also called [[Albedo]], determines how much light it reflects.

**Specular reflection** produces highlights that depend on the viewing direction, such as the reflection seen on polished or shiny surfaces. The Phong reflection model is one way of approximating this behaviour by combining ambient, diffuse and specular components.

### Image Formation

A camera forms an image by controlling which light rays reach its sensor. Without this restriction, light from many different directions would mix together, making it impossible to distinguish the individual objects in a scene.

The [[Pinhole Camera Model]] is a simple way to understand this process. It uses a small opening to allow light rays from different directions to reach specific positions on a projection plane. This creates an image of the scene, although it appears upside down. The size of the opening affects the result: a smaller hole produces a sharper but darker image, while a larger hole allows more light in but makes the image blurrier.

### Types of Projection

A camera maps points from the 3D world onto a 2D image plane. There are different ways to perform this projection.

**Perspective Projection** is the model used by most conventional cameras. Objects become smaller as their distance from the camera increases. This is why distant objects appear smaller than nearby ones.

**Orthographic Projection** uses parallel projection rays instead. The apparent size of an object does not depend on its distance from the camera. This is useful in applications such as industrial measurement, where preserving object dimensions in the image is important. Telecentric lenses are commonly used to approximate this type of projection.

## Resources

_Learn more from external sources._

- [First Principles of Computer Vision – Imaging](https://www.youtube.com/results?search_query=First+Principles+of+Computer+Vision+Imaging)

## Related concepts

_Explore the knowledge network._

- [[Cameras]]
    
- [[Pinhole Camera Model]]
    
- [[Perspective Projection]]
    
- [[Orthographic Projection]]
    
- [[Lambertian Reflection]]
    
- [[Specular Reflection]]
    
- [[Albedo]]
    
- [[Camera Obscura]]