#!/usr/bin/env python
"""
ROS code to make the Neato drive in square 
"""
from geometry_msgs.msg import Twist
import rospy

# we have to initialize ourselves as a roscore
rospy.init_node('drive_square')
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
twist = Twist()

def go():
	print "in go"    
	twist.linear.y = .1    
	pub.publish(twist)    
	rospy.sleep(10)     
 

def turn():
	print "in turn"
	twist.angular.x = 1    
	pub.publish(twist)    
	rospy.sleep(1.5); 	

while not rospy.is_shutdown():     
	go()
	turn()  
