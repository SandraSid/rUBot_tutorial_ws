#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

## ping_pong -> PONG

def pong(msg):
	global a
	counter += msg.data
	new_msg = String		#Define type of message
	new_msg.data = "pong"		#Set message
	pub.publish(new_msg)		#Publish new message
	rospy.loginfo("System answer: : %s", new_message)

rospy.init_node('pong_node')						#Creating a pong node
pub = rospy.Publisher("/pong (topic)", String, queue_size=10)	
sub = rospy.Subscriber("/ping (?)", String, pong)
rospy.spin()
