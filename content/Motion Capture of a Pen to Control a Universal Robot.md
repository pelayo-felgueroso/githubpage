<text>**Semester 2024/2025 · EU4M Mechatronics · SUPMICROTECH, Besançon, France**</text>
## Project Overview

What if you could control a robotic arm simply by moving a pen through the air?

That was the idea behind this project. We developed a motion-tracking system that allows a user to control a Universal Robots UR5e robotic arm by moving a custom-designed stylus.

A camera observes the stylus and tracks its movement in space. The system then translates those movements into commands that the robot can execute in real time.

The goal was to create a more intuitive way for a person to interact with an industrial robot, without having to manually program every movement.

The project brought together mechanical design, computer vision, electronics and robotics, combining hardware and software into a working control system.

## How Does It Work?

The system is built around three main components:

1. **The stylus:** A custom-designed pen equipped with visual references that allow the camera to track its position and orientation.
    
2. **The camera and processing system:** An Intel RealSense D405 captures images and depth information. Computer vision algorithms use this data to estimate the stylus movements.
    
3. **The robotic arm:** A Universal Robots UR5e receives movement commands and reproduces the movements of the stylus.
    

<AsyncImage query="Universal Robots UR5e robotic arm with Intel RealSense depth camera laboratory setup" aspectRatio="16:9"/>

When the user moves the stylus, the camera captures its movement. The software processes the images, estimates the stylus pose and converts it into coordinates for the robot. These coordinates are then sent to the UR5e, which follows the corresponding movements.

## System Development

### 1. Stylus Design and Manufacturing

The stylus was designed to be comfortable to hold while providing reliable visual references for the tracking algorithms.

It features four reference spheres arranged asymmetrically along its body. Their different positions make it possible to distinguish the stylus in space and determine how it is oriented.

An ArUco marker was also incorporated as an alternative visual tracking method.

The design was created in SolidWorks and manufactured using 3D printing. The assembly includes a positioning key to prevent the spheres from rotating, an M3 brass threaded insert and an M3 screw.

The reference spheres were painted matte white to improve visibility and reduce unwanted reflections.

<AsyncImage query="custom 3D printed motion capture tracking stylus with four white spheres and ArUco marker" aspectRatio="16:9"/>

### 2. Camera Support and Lighting

A stable camera position is essential for accurate motion tracking.

We designed a mounting structure for the Intel RealSense D405 using 4 mm acrylic sheets. The parts were designed in CAD, cut using a laser cutter and mounted onto a 20 × 20 mm aluminium profile.

The structure also includes a circular LED light to provide more consistent illumination during image capture.

During testing, the horizontal support showed some oscillation. We added lateral acrylic reinforcements to improve rigidity and reduce vibrations.

<AsyncImage query="laser cut acrylic Intel RealSense camera mounting bracket aluminium extrusion engineering project" aspectRatio="16:9"/>

### 3. Control Panel Design

We also designed a physical control panel to house the system electronics and provide an interface for the operator.

The enclosure was designed around a Raspberry Pi 4 Model B and a connection board. It includes:

- An LCD screen.
    
- Physical control buttons.
    
- Status LEDs.
    
- A dead-man switch.
    
- Ventilation openings.
    
- Access to the required ports and connections.
    

The enclosure was modelled in SolidWorks and manufactured using 3D printing. Its design was divided into a main body and a removable top cover to make assembly and access to the electronics easier.

<AsyncImage query="3D printed Raspberry Pi electronics control panel enclosure LCD buttons LEDs engineering prototype" aspectRatio="16:9"/>

### 4. Camera-Based Motion Tracking

The tracking system uses an Intel RealSense D405 RGB-D camera.

An RGB-D camera captures two types of information:

- **RGB image:** A normal colour image.
    
- **Depth image:** Information about how far objects are from the camera.
    

Combining both allows the system to identify visual features in an image and estimate their positions in three-dimensional space.

We developed two complementary approaches to track the stylus.

#### Sphere Tracking

The first approach uses the four white spheres attached to the stylus.

The image-processing pipeline identifies the spheres by analysing their colour and brightness. OpenCV is used to process the images, isolate potential sphere regions and detect their contours.

Once detected, the centre of each sphere can be estimated in the image. Depth information is then used to recover their spatial positions.

By combining the positions of the four spheres, the system can estimate the position and orientation of the stylus.

<AsyncImage query="computer vision white sphere detection OpenCV binary mask contour tracking camera image" aspectRatio="16:9"/>

#### ArUco Marker Tracking

The second approach uses an ArUco marker attached to the stylus.

ArUco markers are visual patterns that can be recognised by a camera. Because their geometry and physical size are known, they can be used to estimate the position and orientation of an object relative to the camera.

We implemented marker detection and pose estimation using OpenCV. The resulting position and orientation information provides another way to track the stylus.

Using two different tracking approaches allowed us to explore alternative ways of estimating the stylus movement.

<AsyncImage query="OpenCV ArUco marker pose estimation camera image coordinate axes" aspectRatio="16:9"/>

### 5. Stylus Position and Orientation

Detecting the stylus in an image is only the first step. To control a robot, the system needs to understand how the stylus is positioned and oriented in three-dimensional space.

The tracking information is processed to estimate the position of the stylus tip and its orientation.

We also developed a geometric simulation in Python using NumPy, SciPy and Matplotlib. It was used to study the relationship between the reference points on the stylus, its orientation and the position of its tip.

This provided a way to test and visualise the geometry behind the tracking system.

<AsyncImage query="Python Matplotlib 3D geometric simulation stylus pen orientation coordinate axes" aspectRatio="16:9"/>

### 6. Robot Communication and Control

The final stage connects the tracking system to the physical robotic arm.

We used the RTDE interface (Real-Time Data Exchange) to communicate with the Universal Robots UR5e through Python.

The estimated stylus movements are transformed into the robot's coordinate system and converted into Cartesian movement commands.

The robot can then reproduce the movements of the stylus in real time.

This is what brings the different parts of the project together: the physical stylus, camera-based tracking, coordinate transformations and robot control.

<AsyncImage query="Universal Robots UR5e robot arm laboratory robotic manipulation demonstration" aspectRatio="16:9"/>

### 7. Electronics and User Interface

The electronic system was built around a Raspberry Pi 4 Model B.

We designed and prototyped the control electronics, including the connections for the buttons and status LEDs. The PCB was designed using EasyEDA, and the circuit was assembled and tested.

We also designed a graphical user interface to provide information about the system and allow the operator to interact with it.

The interface included operating status, robot status, movement speed, notifications and different operating modes:

- **Echo:** Reproduces the stylus movements.
    
- **Real-time:** Provides direct movement control.
    
- **Scale:** Applies a scaling factor to the movements.
    
- **Mirror:** Mirrors the movements.
    

<AsyncImage query="custom PCB electronics Raspberry Pi control interface prototype" aspectRatio="16:9"/>

<AsyncImage query="Figma robotic arm control dashboard GUI interface prototype" aspectRatio="16:9"/>
## Technologies and Tools

|Area|Technologies|
|---|---|
|Mechanical design|SolidWorks, 3D printing, laser cutting|
|Camera and sensing|Intel RealSense D405, RGB-D imaging|
|Computer vision|Python, OpenCV, ArUco markers|
|Geometry and simulation|NumPy, SciPy, Matplotlib|
|Robot communication|Universal Robots UR5e, RTDE, `ur_rtde`|
|Electronics|Raspberry Pi 4, EasyEDA, PCB prototyping|
|User interface|Figma|

## Project Outcome

The project resulted in a working motion-capture system capable of controlling a Universal Robots UR5e robotic arm through the movement of a custom-designed stylus.

We brought together the mechanical, electronic and software components needed to make this interaction possible, from designing and manufacturing the stylus to tracking its movement and translating it into robot commands.

One of the most interesting aspects of the project was seeing how different engineering disciplines had to work together to solve a single problem. Mechanical design, camera calibration, computer vision, coordinate transformations and robot control were all essential parts of the same system.

The project gave me practical experience in developing a complete robotic application, working across hardware and software and turning an initial concept into a physical system.

## Project Information

- **Project:** Motion Capture of a Pen to Control a Universal Robot
    
- **Academic year:** 2024/2025
    
- **Programme:** EU4M Mechatronics
    
- **Institution:** SUPMICROTECH, Besançon, France
    
- **Robot:** Universal Robots UR5e
    
- **Camera:** Intel RealSense D405