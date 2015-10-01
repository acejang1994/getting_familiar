#!/usr/bin/env python

"""
ROS Code for publishing topic where Neato robot moves in space
"""

from geometry_msgs.msg import Twist, Vector3

import rospy
import tty
import select
import sys
import termios

settings = termios.tcgetattr(sys.stdin)

# Gets ascii value of keyboard hits
def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

# Initiate node and topic, as well as time rate
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.init_node('teleop_tranport')
r = rospy.Rate(10)
key = None

# Loop for operation
while not rospy.is_shutdown():
	key = getKey()
	linObj = Vector3()
	angObj = Vector3()

	# Key-based transformation
	if key == 'w':
	    linObj.x = 0.2
	elif key == 'a':
	    angObj.z = 0.4
	elif key == 's':
	    linObj.x = -0.2
	elif key == 'd':
	    angObj.z = -0.4
	elif key == 'x':
		linObj.x = 0.0
		angObj.x = 0.0

	# Publishes Twist Object and waits
	disp = Twist(linObj, angObj)
	pub.publish(disp)
	r.sleep()

	if (key == '\x03'):
	    break