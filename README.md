# ROS-turtle-mirror


This repository contains the ROS turtlesim mirror projet that I did for the task round of the [Autonomous Ground Vehicle Research Group-IIT KGP](https://github.com/AGV-IIT-KGP).
This project consists of launching two turtlesim nodes at the same time using roslaunch and then running a node such that one turtlevertically mirrors the other one.
In this project I went ahead and created an xml launch file which is used to launch multiple nodes at the same time and used it to launch two groups namely- /turtlesim1/turtle1/ and turtlesim2/turtle1/. After that I wrote a python script which can be found here as rotate.py which is used to initially place the turtles heading opposite to one another or in other words, the pose.theta difference between the two turtlesim nodes will be pie radians.
Following the rotate.py, I scripted the mirror.py which publishes to /turtlesim2/turtle1/cmd_vel the exact mirror conditions of /turtlesim1/turtle1/cmd_vel. The velocity of turtle1 is read from an input by the user every time the node is called using rosrun.

The following is an image of the simulator in working condition:

![image1](https://user-images.githubusercontent.com/81582740/122183212-a3087480-cea8-11eb-8aff-8102be1fca22.png)


References:[ROS Wiki](http://wiki.ros.org/ROS/Tutorials)
           
