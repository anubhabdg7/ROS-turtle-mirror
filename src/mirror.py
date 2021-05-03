#!/usr/bin/env python3

# Author-anubhab

import rospy
from geometry_msgs.msg import Twist
import math
from turtlesim.msg import Pose

def mirror_t():
    rospy.init_node('robot',anonymous=True)
    vel_pub=rospy.Publisher('/turtlesim2/turtle1/cmd_vel',Twist,queue_size=10)
    vel_pub1=rospy.Publisher('/turtlesim1/turtle1/cmd_vel',Twist,queue_size=10)
    v=Twist();
    
    print("Here turtle 2 will mirror turtle 1.You have to input the speed of movement of turtle 1")
    vx=input("Input the linear speed in x-direction")
    vy=input("Input the linear speed in y-direcion")
    vz=input("Input the angular speed in the z-direction")
    v.linear.x=float(vx)
    v.linear.y=float(vy)
    v.linear.z=0
    v.angular.x=0
    v.angular.y=0
    v.angular.z=float(vz)
    vel_pub1.publish(v)
    v.linear.x=(1*float(vx))
    v.linear.y=-1*float(vy)
    v.angular.z=-1*float(vz)
    vel_pub.publish(v)
    rospy.spin()

if __name__ == '__main__':
    
        try:
            mirror_t()
        except rospy.ROSInterruptException: pass








