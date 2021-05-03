#!/usr/bin/env python3

# Author-anubhab

import rospy
import math
from geometry_msgs.msg import Twist

def rotate():
    rospy.init_node('robo',anonymous=True)
    vel=rospy.Publisher('/turtlesim2/turtle1/cmd_vel',Twist,queue_size=10)
    v=Twist()
    v.linear.x=0
    v.linear.y=0
    v.linear.z=0
    v.angular.x=0
    v.angular.y=0
    v.angular.z=0.5
    t0=rospy.Time.now().to_sec()
    current_angle=0.00
    while(current_angle<2.700):
        vel.publish(v)
        t1=rospy.Time.now().to_sec()
        current_angle=0.5*(t1-t0)
    v.angular.z=0
    rospy.spin()

if __name__ == '__main__':
    try:
        rotate()
    except rospy.ROSInterruptException: pass
