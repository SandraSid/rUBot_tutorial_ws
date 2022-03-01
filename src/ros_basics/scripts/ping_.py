#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

##Script for the phyton publisher

rospy.init_node("ping_node", anonymous=True)  	#Create a ping node
pub = rospy.Publisher("/ping", String, queue_size=10) #Publish a String type message
							#in /ping topic
rate = rospy.Rate(1)					#Each second

##Message to send
while not rospy.is_shutdown():
	msg = String
	msg.data = ping
	pub.publish(msg)
	rate.sleep()
