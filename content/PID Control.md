## Explanation

PID (Proportional-Integral-Derivative) control is a feedback control method used to make a system reach and maintain a desired state, such as a robot joint reaching a specific angle or maintaining a certain velocity.

The controller continuously compares the desired value (setpoint) with the measured value and calculates the error. It uses three terms to determine how to correct it:

- **Proportional (P):** Reacts to the current error. A larger error produces a stronger correction.
    
- **Integral (I):** Considers the accumulated error over time. It helps eliminate small errors that remain even after the proportional correction.
    
- **Derivative (D):** Considers how quickly the error is changing. It helps anticipate changes and reduce overshoot.
    

The three terms are combined to calculate the control output. Their contribution is adjusted using three gains: Kp, Ki and Kd. Choosing these gains is known as PID tuning.

PID controllers are widely used in robotics for controlling joint position, velocity and motor speed. They are relatively simple and effective, although their performance depends on proper tuning and the characteristics of the system.
## Resources

_Learn more from external sources._

- [Mike Likes Robots – Understanding PID Controllers](https://www.youtube.com/watch?v=z50ZXCzaVoI)
## Related concepts

_Explore the knowledge network._

- [[Robot Control]]
    
- [[Actuators]]
    
- [[Robot Joints]]
    
- [[Sensors]]
    
- [[Kinematics]]
    
- [[Motion Planning]]