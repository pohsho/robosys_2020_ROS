#! /usr/bin/env python3
import rospy
import random
from std_msgs.msg import Int32

janken_fight = ["グー","チョキ","パー"]

Player_2 = random.randint(0,2)

Player_1 = 0

def cb(message):
    global Player_1
    Player_1 = message.data


    if Player_1 == Player_2:
        rospy.loginfo('drow')

    elif Player_1 ==0:
        if Player_2 == 1:
            rospy.loginfo('YouWin!!!')
        elif Player_2 == 2:
            rospy.loginfo('YouLose!!!!!!!!!!')

    elif Player_1 == 1:
        if Player_2 == 0:
            rospy.loginfo('YouLose!!!!!!!!')
        elif Player_2 == 2:
            rospy.loginfo('YouWin!!!')

    elif Player_1 == 2:
        if Player_2 == 0:
            rospy.loginfo('YouWin!!!')
        elif Player_2 == 1:
            rospy.loginfo('YouLose!!!!!!!!!!!')



def janken_number():
    if p == 0:
        rospy.loginfo('Rock')

    elif p == 1:
        rospy.loginfo('Scissors')

    else :
        rospy.loginfo('paper')



if __name__=='__main__':
    rospy.init_node('Player_2')
    sub = rospy.Subscriber('janken_fight', Int32, cb)
    pub = rospy.Publisher('janken_result', Int32, queue_size=1)
    rate = rospy.Rate(1.0)

while not rospy.is_shutdown():
    rate.sleep()
