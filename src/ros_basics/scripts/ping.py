#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

## ping_pong -> PING

rospy.init_node('ping_node', anonymous=True)  		#Create a ping node
pub = rospy.Publisher('/ping_topic', String, queue_size=10) 	#Publish a String type message
								#in /ping topic
rate = rospy.Rate(1)						#Each second

## Message to send

while not rospy.is_shutdown():
	msg = String			#Definetype of message
	str_ping = "ping"		#Create message
	rospy.loginfo(str_ping)
	msg.data = str_ping		#Set message
	pub.publish(msg)		#Publish message
	rate.sleep()			##Wait untill new
