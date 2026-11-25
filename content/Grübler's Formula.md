## Explanation

Grübler's Formula, also known as the Grübler-Kutzbach criterion, is used to calculate the mobility, or number of degrees of freedom, of a mechanical mechanism. It estimates how many independent movements are possible based on the number of links and joints in a mechanism.

The formula has different forms depending on whether the mechanism is planar or spatial.

### Planar mechanisms

For a planar mechanism, the formula is:

$$  
M = 3(n-1) - 2j_1 - j_2  
$$

Where:

- ($M$) is the mobility or number of degrees of freedom.
    
- ($n$) is the total number of links, including the fixed link.
    
- ($j_1$) is the number of joints that allow one relative movement, such as revolute or prismatic joints.
    
- ($j_2$) is the number of joints that allow two relative movements.
    

### Spatial mechanisms

For a spatial mechanism, the Chebychev-Grübler-Kutzbach criterion is:

$$  
M = 6(n-1-j) + \sum_{i=1}^{j} f_i  
$$

Where:

- ($M$) is the mobility or number of degrees of freedom.
    
- ($n$) is the total number of links, including the fixed link.
    
- ($j$) is the total number of joints.
    
- ($f_i$) is the number of degrees of freedom allowed by joint ($i$).
    

The factor 6 accounts for the six possible relative degrees of freedom of a rigid body in three-dimensional space: three translational and three rotational movements.

For example, a revolute or prismatic joint allows one relative degree of freedom, while a spherical joint allows three.

### Application in robotics

The spatial formulation is particularly relevant to serial robotic manipulators. For example, the UR5e has six revolute joints, each allowing one rotational degree of freedom. Its six joints provide six independently actuated joint coordinates, allowing the robot to control its end-effector pose within its workspace.

For the UR5e, the spatial mobility criterion gives:

$$  
M = 6(7-1-6) + 6(1)  
$$

$$  
M = 6  
$$

This confirms that the robot has six degrees of freedom.

However, the mobility criterion alone does not guarantee that a mechanism can reach every possible pose. Workspace limitations, joint constraints and singular configurations must also be considered.

Both formulations are useful during the design and analysis of mechanisms to estimate their mobility and determine how many independent inputs are needed to control their movement.

The formulas assume ideal rigid links and joints. Special configurations, redundant constraints and dependent constraints can make the actual mobility differ from the calculated value.

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