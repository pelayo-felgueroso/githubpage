<text>**Semester 2024/2025 · EU4M Mechatronics · SUPMICROTECH, Besançon, France**</text>  
## Project Overview

**What if you could control a robotic arm simply by moving a pen through the air?**

That was the idea behind this project. We developed a motion-tracking system that allows a user to control a Universal Robots UR5e robotic arm by moving a custom-designed stylus.

A camera observes the stylus and tracks its movement in space. The system then translates those movements into commands that the robot can execute in real time.

The goal was to create a more intuitive way for a person to interact with an industrial robot, without having to manually program every movement.

The project brought together mechanical design, computer vision, electronics and robotics, combining hardware and software into a working control system.

![Complete motion-tracking setup: camera mount, stylus and UR5e](images/setup.jpg)

## How Does It Work?

The system is built around three main components:

1. **The stylus:** A custom-designed pen equipped with visual references that allow the camera to track its position and orientation.
2. **The camera and processing system:** An Intel RealSense D405 captures images and depth information. Computer vision algorithms use this data to estimate the stylus movements.
3. **The robotic arm:** A Universal Robots UR5e receives movement commands and reproduces the movements of the stylus.

When the user moves the stylus, the camera captures its movement. The software processes the images, estimates the stylus pose and converts it into coordinates for the robot. These coordinates are then sent to the UR5e, which follows the corresponding movements.

## System Development

### 1. Stylus Design and Manufacturing

The stylus was designed to be comfortable to hold while providing reliable visual references for the tracking algorithms.

It features four reference spheres arranged asymmetrically along its body. Their different positions make it possible to distinguish the stylus in space and determine how it is oriented. An ArUco marker was also incorporated as an alternative visual tracking method.

The assembly includes a positioning key to prevent the spheres from rotating, an M3 brass threaded insert and an M3 screw.

<model-viewer src="./images/stylus.glb" alt="3D model of the custom-designed tracking stylus" camera-controls auto-rotate camera-orbit="225deg 75deg 105%" shadow-intensity="1" exposure="1" style=" width: 100%; height: 450px; background-color: var(--light); border-radius: 12px; "> </model-viewer>

_Interactive 3D model of the stylus. Drag to rotate._

The design was created in SolidWorks and manufactured using 3D printing. The reference spheres were painted matte white to improve visibility and reduce unwanted reflections.

![Custom-designed tracking stylus](images/3dprint.jpg)  
### 2. Camera Support and Lighting

A stable camera position is essential for accurate motion tracking.

We designed a mounting structure for the Intel RealSense D405 using 4 mm acrylic sheets. The parts were designed in CAD, cut using a laser cutter and mounted onto a 20 × 20 mm aluminium profile.

The structure also includes a circular LED light to provide more consistent illumination during image capture, and lateral acrylic reinforcements to improve rigidity and reduce vibrations.

![Camera support with the RealSense D405 and LED ring, bottom view](images/soporte_bot.jpg)

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

![Control panel enclosure](images/controler4.jpg)

### 4. Camera-Based Motion Tracking

The tracking system uses an Intel RealSense D405 RGB-D camera, which captures a colour image and a depth image of the scene. Combining both allows the system to identify visual features in the image and estimate their positions in three-dimensional space.

We developed two complementary approaches to track the stylus.

#### Sphere Tracking

The first approach uses the four white spheres attached to the stylus.

The image-processing pipeline identifies the spheres by analysing their colour and brightness. OpenCV is used to process the images, isolate potential sphere regions and detect their contours.

Once detected, the centre of each sphere can be estimated in the image. Depth information is then used to recover their spatial positions.

By combining the positions of the four spheres, the system can estimate the position and orientation of the stylus.

![Detection of the four reference spheres with their 3D coordinates](images/balls.jpg)

#### ArUco Marker Tracking

The second approach uses an ArUco marker attached to the stylus.

ArUco markers are visual patterns that can be recognised by a camera. Because their geometry and physical size are known, they can be used to estimate the position and orientation of an object relative to the camera.

We implemented marker detection and pose estimation using OpenCV. The resulting position and orientation information provides another way to track the stylus.

Using two different tracking approaches allowed us to explore alternative ways of estimating the stylus movement.

![ArUco marker detection and pose estimation](images/tracking.jpg)

### 5. Stylus Position and Orientation

Detecting the stylus in an image is only the first step. To control a robot, the system needs to understand how the stylus is positioned and oriented in three-dimensional space.

The tracking information is processed to estimate the position of the stylus tip and its orientation.

We also developed a geometric simulation in Python using NumPy, SciPy and Matplotlib. It was used to study the relationship between the reference points on the stylus, its orientation and the position of its tip.

This provided a way to test and visualise the geometry behind the tracking system.

### 6. Robot Communication and Control

The final stage connects the tracking system to the physical robotic arm.

We used the RTDE interface (Real-Time Data Exchange) to communicate with the Universal Robots UR5e through Python.

The estimated stylus movements are transformed into the robot's coordinate system and converted into Cartesian movement commands.

The robot can then reproduce the movements of the stylus in real time.

This is what brings the different parts of the project together: the physical stylus, camera-based tracking, coordinate transformations and robot control.

### 7. Electronics and User Interface

The electronic system was built around a Raspberry Pi 4 Model B.

We designed and prototyped the control electronics, including the connections for the buttons and status LEDs. The PCB was designed using EasyEDA, and the circuit was assembled and tested.

![PCB for the control panel electronics](images/pcb.jpg)

We also designed a graphical user interface to provide information about the system and allow the operator to interact with it.

The interface included operating status, robot status, movement speed, notifications and different operating modes:

- **Echo:** Reproduces the stylus movements.
- **Real-time:** Provides direct movement control.
- **Scale:** Applies a scaling factor to the movements.
- **Mirror:** Mirrors the movements.

![Graphical user interface with the operating modes](images/gui.jpg)

## Project Outcome

The project resulted in a working motion-capture system capable of controlling a Universal Robots UR5e robotic arm through the movement of a custom-designed stylus.

We brought together the mechanical, electronic and software components needed to make this interaction possible, from designing and manufacturing the stylus to tracking its movement and translating it into robot commands.

One of the most interesting aspects of the project was seeing how different engineering disciplines had to work together to solve a single problem. Mechanical design, camera calibration, computer vision, coordinate transformations and robot control were all essential parts of the same system.

![System overview](images/esquema.jpg)

The project gave me practical experience in developing a complete robotic application, working across hardware and software and turning an initial concept into a physical system.

<video src="./images/demo.mp4" controls muted playsinline loop style="width: 100%; border-radius: 12px;"></video>

_Me operating the UR5e with the custom stylus. Echo operating mode (Reproduces the stylus movements)_

## My Contribution

This was a four-person team project. I defined the physical concept of the system: how the setup would be arranged, how the stylus would be tracked and where the camera would be mounted. I then designed and built all the mechanical components, from the first sketches through CAD, manufacturing and assembly.

Because the mechanical design had a direct effect on tracking performance, I worked closely with the motion-tracking side of the project. I designed the stylus geometry the tracking relied on: the reference spheres, their spacing and the asymmetric layout that makes the pose identifiable, plus an ArUco marker as a second tracking method. I also decided the mounting height of the camera above the table together with the vision team, so that the camera's working range and field of view covered the user's workspace with reliable depth data.

<style> .gallery { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 1.5rem 0; } .gallery figure { margin: 0; } .gallery img { width: 100%; height: auto; border-radius: 8px; } .gallery figcaption, .hero figcaption { font-size: 0.85rem; text-align: center; opacity: 0.8; } .hero { margin: 1.5rem 0; } .hero img { width: 100%; height: auto; border-radius: 8px; } </style>

### System Concept and User Interaction

Before designing any part, I sketched how the user would hold and move the stylus, how it would be tracked, and how the setup would be arranged: the camera mounted above the workspace, the user moving the stylus in front of it, the UR5e reproducing the motion, and a control panel next to the operator.

I designed the interaction around safety and simplicity. The operator controls the system from the panel, can switch between operating modes, and must hold a dead-man switch for the robot to move, so that releasing it stops the robot.

<figure class="hero"> <img src="./images/concepto_stylet.jpg" alt="Hand-drawn concept of the stylus in use"> <figcaption>Hand-drawn concept of the stylus in use, the starting point of the design</figcaption> </figure>

### Tracking Stylus

I benchmarked existing styluses (Apple Pencil: 157 × 9 mm; Wacom Intuos 4 Grip Pen: 151 × 12.7 mm) and chose a length of 150 mm for familiar handling and a diameter of 18 mm for a firm grip during long use.

<figure class="hero"> <img src="./images/comp.jpg" alt="Size comparison with Apple Pencil and Wacom Intuos 4 Grip Pen"> <figcaption>Size comparison with existing styluses</figcaption> </figure>

I designed the tracking geometry together with the vision requirements. The four reference spheres are placed **asymmetrically**, at 36, 51, 36 and 66 mm from the centre, so that each sphere can be identified and the stylus orientation is unambiguous. An ArUco marker provides a second, redundant tracking method in case spheres are occluded.

<figure class="hero"> <img src="./images/boceto_pre.jpg" alt="Hand-drawn concept of the stylus in use"> <figcaption>Hand-drawn sketch of the exploded assembly</figcaption> </figure>

<div class="gallery"> <figure><img src="./images/aruco.jpg" alt="ArUco marker integrated in the stylus"><figcaption>Integrated ArUco marker</figcaption></figure> <figure><img src="./images/reff.jpg" alt="Asymmetrical sphere layout, numbered"><figcaption>Asymmetrical sphere layout</figcaption></figure></div>

Details that made the tracking reliable:

- A **key** that prevents the sphere attachment from rotating, so the known geometry used by the pose estimation never changes.
- An **M3 brass threaded insert and a DIN 912 M3×16 screw** for a robust, removable joint, hidden under the ArUco marker.
- **Matte RAL 9010 white** paint on the spheres, with the rest of the body masked, for maximum contrast and minimal reflections.

<figure class="hero"> <img src="./images/boceto.jpg" alt="Hand-drawn concept of the stylus in use"> <figcaption>Hand-drawn sketch of the exploded assembly</figcaption> </figure>

<div class="gallery"><figure><img src="./images/exploded_view.jpg" alt="Exploded view showing the anti-rotation key"><figcaption> Exploded view in CAD</figcaption></figure> <figure><img src="./images/stylet_nopaint.jpg" alt="3D printed before painting"><figcaption>3D Printed fuully assembled before painting</figcaption></figure> </div>

The stylus was modelled in SolidWorks, 3D printed, assembled and painted.

<div class="gallery"> <figure><img src="./images/painting_process.jpg" alt="Painting the reference spheres"><figcaption>Painting the spheres (body masked)</figcaption></figure> <figure><img src="./images/pint.jpg" alt="Final stylus with painted spheres"><figcaption>Final stylus</figcaption></figure> </div>

### Camera Support

I designed the mount for the Intel RealSense D405 in **laser-cut 4 mm acrylic** on a 20×20 mm aluminium profile, with the needs of the vision system in mind:

- **Mounting height:** I defined the height of the camera mount above the table together with the vision team, balancing the depth camera's optimal working distance against the field of view needed to cover the user's movements.
- **Primary support** with camera fixation points and radial holes for a **circular LED ring**, giving uniform lighting on the spheres and reducing shadows and detection errors.
- **Spacers** that position the camera just below the LED ring and keep clearance for its cable.

<div class="gallery"> <figure><img src="./images/top.jpg" alt="Primary support with LED ring, top view"><figcaption>Primary support, top view</figcaption></figure> <figure><img src="./images/bot.jpg" alt="Primary support with camera, bottom view"><figcaption>Primary support with camera, bottom view</figcaption></figure> </div>

During testing I found that the horizontal bar oscillated, which degraded the depth data. I sketched curved **lateral reinforcements** directly over a photo of the structure, turned them into DXF files for laser cutting and mounted them, which eliminated the vibration.

<div class="gallery"> <figure><img src="./images/supports.jpg" alt="Reinforcement sketched over a photo of the structure"><figcaption>Reinforcement sketched on the real structure</figcaption></figure> <figure><img src=".images/lat.jpg" alt="Lateral reinforcement part"><figcaption>Final reinforcement part</figcaption></figure> </div> <figure class="hero"> <img src="./images/soporte_lat.jpg" alt="Final camera support mounted on the aluminium profile"> <figcaption>Final assembly on the aluminium profile, with the reinforcements in place</figcaption> </figure>

### Control Panel

I designed the operator's panel, which also houses the electronics:

- A **main box** for the Raspberry Pi 4 and the connection board, with the LCD above, cutouts for all ports and lateral ventilation slots.
- A **removable top cover** with the control buttons, five status LEDs and the dead-man switch, fastened with M3×12 screws into 3 mm inserts for easy maintenance.

<figure class="hero"> <img src="./images/boceto_mando.jpg" alt="Hand-drawn concept of the control panel"> <figcaption>Hand-drawn concept of the control panel</figcaption> </figure> <div class="gallery"> <figure><img src="./images/diseno_final_mando_2.jpg" alt="Control panel, top view"><figcaption>Top view</figcaption></figure> <figure><img src="./images/diseno_final_mando_1.jpg" alt="Control panel, side view with ports and ventilation"><figcaption>Ports and ventilation</figcaption></figure></div>

### What I Took from It

Designing the physical system of a vision-controlled robot taught me that hardware and computer vision cannot be designed separately. Sphere placement, surface finish, lighting and structural stiffness all decided how well the camera could track the stylus. Designing for the vision system, and seeing the robot follow my own hand movements with the stylus I had designed, was the most rewarding part of the project.

## Project Information

- **Project:** Motion Capture of a Pen to Control a Universal Robot
- **Academic year:** 2024/2025
- **Programme:** EU4M Mechatronics
- **Institution:** SUPMICROTECH, Besançon, France
- **Team:** 4 students
- **My role:** System concept and mechanical design; stylus geometry and camera placement for motion tracking
- **Robot:** Universal Robots UR5e
- **Camera:** Intel RealSense D405