## Explanation

Grübler's Formula is used to calculate the mobility, or number of degrees of freedom, of a mechanical mechanism. It estimates how many independent movements are possible based on the number of links and joints in a mechanism.

For a planar mechanism, the formula is:


$$
M = 3(n-1) - 2j_1 - j_2
$$
Where:

- ($M$) is the mobility or number of degrees of freedom.
- ($n$) is the total number of links, including the fixed link.
- ($j_1$) is the number of joints that allow one relative movement, such as revolute or prismatic joints.
- ($j_2$) is the number of joints that allow two relative movements.

It is useful during the design of mechanisms to check how many independent inputs are needed to control their movement.

The formula assumes a planar mechanism with standard joints. Special configurations and redundant constraints can make the actual mobility different from the calculated value.

## Resources

_Learn more from external sources._

- [Northwestern Robotics – Modern Robotics, Chapter 2.2: Degrees of Freedom of a Robot](https://www.youtube.com/watch?v=zI64DyaRUvQ)
## Related concepts

_Explore the knowledge network._

- [[Robot Mechanics]]
    
- [[Robot Links]]
    
- [[Degrees of Freedom (DOF)]]
    
- [[Actuators]]
    
- [[Electric Motors]]
    
- [[Kinematics]]
    
- [[Forward Kinematics]]