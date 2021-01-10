#! /usr/bin/env python3
import rospy
import random
from std_msgs.msg import Int32

hands = ["グー", "チョキ", "パー"]

print("0:グー　1:チョキ　2:パー")
p = int(input(""))
player = hands[p]

if __name__=='__main__':
    rospy.init_node('player_1')
    pub = rospy.Publisher('janken_fight', Int32, queue_size=1)
    rate = rospy.Rate(0.5)

while not rospy.is_shutdown():
    pub.publish(p)
    rate.sleep()

