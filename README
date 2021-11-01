## Table of Contents
*[General info](#general-info)
*[Technologies](#technologies)
*[Setup](#setup)
*[Visualizing Lidar output](#Visualizing-Lidar-output)
*[Teleoperation](#Teleoperation)
*[Publisher Subscriber](#Publisher-Subscriber)
 
## General info
ROS package for a simple four wheeled steerable robot.

## Technologies
Project is created with:
* Ubuntu 18.04
* ROS Melodic
* Python3

## Setup
To run this project, clone it to src folder of your catkin workspace and run:

```
$ catkin_make clean && catkin_make
$ source ~/catkin_ws/devel/setup.bash

```

## Visualizing Lidar output
To see the Lidar output,run:

```
$ roslaunch car template_launch.launch
```

In a new terminal run:

```
$ rviz
```

Add the Laser sensor and in the Topic menu select: /car/scan


 
## Teleoperation
Helps control the motion of the robot using keyboard. 
Open a terminal and run:

```
$ roscore
```

In a new terminal run:

```
$ roslaunch car template_launch.launch
```

In a new terminal run the below commands and follow the instructions in the terminal to control the model:

```
$ cd ~/catkin_ws/src/car
$ python3 teleop_template.py
```



## Publisher-Subscriber
Runs the robot in a specified path.
Open a terminal and run:

```
$ roscore
```

In a new terminal run:

```
$ roslaunch car template_emptyworld.launch
```

To run the publisher, run the following in a new terminal:

```
$ cd ~/catkin_ws/src/car/scripts
$ python3 pub.py
```

To run the subscriber, run the following in a new terminal:

```
$ cd ~/catkin_ws/src/car/scripts
$ python3 sub.py
```
