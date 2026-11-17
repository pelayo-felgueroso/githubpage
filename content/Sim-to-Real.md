## Explanation

Sim-to-Real refers to the process of transferring a model, controller or policy developed in simulation to a physical robot.

Simulation allows robotic systems to be tested and trained in a controlled environment, often with faster iterations and lower costs. However, a simulated robot is never a perfect representation of the real world.

Differences can appear in physics, friction, sensor noise, lighting, camera properties and actuator behaviour. These differences are commonly known as the sim-to-real gap.

Several techniques can help reduce this gap. One example is domain randomization, where different physical and visual conditions are introduced during training so that the model becomes more robust to variations. Another approach is system identification, where the simulation parameters are adjusted to better match the behaviour of the real robot.

Sim-to-real transfer is particularly important in [[Robot Learning]], where policies trained in simulation need to work reliably on real hardware.

Even after training, a model needs to be tested carefully on the physical robot. Small differences in timing, calibration or sensor measurements can lead to unexpected behaviour.

## Resources

_Learn more from external sources._

- [NVIDIA Isaac Lab – Documentation](https://isaac-sim.github.io/IsaacLab/)
    
- [NVIDIA Isaac Sim – Domain Randomization](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html)
    
- [Hugging Face – LeRobot](https://huggingface.co/docs/lerobot/en/index)

## Related concepts

- [[Robot Simulation]]
    
- [[Robot Learning]]
    
- [[Imitation Learning]]
    
- [[Sensors]]
    
- [[Robotics]]
    
- [[VLA]]