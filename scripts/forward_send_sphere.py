#!/usr/bin/env python
"""
ROS node that publishes 10 times a second a message of type visualization_messages/Marker.
"""

from visualization_msgs.msg import Marker
from std_msgs.msg import Header
from geometry_msgs.msg import PointStamped, Point, Pose
import rospy

# we have to initialize ourselves as a roscore
rospy.init_node('push_message')

marker = Marker()
marker.header.frame_id = "base_link"

marker.action = marker.ADD
marker.type = marker.SPHERE
marker.pose.position.x = 1
marker.pose.position.y = 0
marker.pose.position.z = 0
marker.pose.orientation.w = 1.0
marker.scale.x = .3
marker.scale.y = .3
marker.scale.z = .3
marker.color.a = 1.0
marker.color.r = 1.0
marker.color.g = 1.0
marker.color.b = 1.0


pub = rospy.Publisher("/our_sphere", Marker, queue_size=10)

r = rospy.Rate(10)

while not rospy.is_shutdown():
	pub.publish(marker)
	r.sleep()


