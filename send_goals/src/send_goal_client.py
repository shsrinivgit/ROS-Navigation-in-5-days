#! /usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionResult, MoveBaseFeedback

class sending_goal():
    feedback = MoveBaseFeedback
    def __init__(self):
        self.client = actionlib.SimpleActionClient('/move_base',MoveBaseAction)
        rospy.loginfo('wait_for_server')
        self.client.wait_for_server()
        rospy.loginfo('server found')
        self.goal = MoveBaseGoal()
        rospy.sleep(0.5)
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.z = 0
        self.goal.target_pose.pose.orientation.x = 0
        self.goal.target_pose.pose.orientation.y = 0
        self.goal.target_pose.pose.orientation.z = 0.75
        self.goal.target_pose.pose.orientation.w = 0.66
    
    def pose1(self):
        self.goal.target_pose.pose.position.x = 1
        self.goal.target_pose.pose.position.y = -4
        return self.goal
    def pose2(self):
        self.goal.target_pose.pose.position.x = 2
        self.goal.target_pose.pose.position.y = -2
        return self.goal
    def pose3(self):
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.x = 1
        self.goal.target_pose.pose.position.y = -3
        return self.goal

    def callback(self, feedback):
        print(feedback)
    
    def sending(self):
        while not rospy.is_shutdown():
            self.pose1()
            self.client.send_goal(self.goal, feedback_cb=self.callback)
            self.client.wait_for_result()
            rospy.loginfo('moved to pose 1')

            self.pose2()
            self.client.send_goal(self.goal,feedback_cb=self.callback)
            self.client.wait_for_result()
            rospy.loginfo('moved to pose 2')

            self.pose3()
            self.client.send_goal(self.goal,feedback_cb=self.callback)
            self.client.wait_for_result()
            rospy.loginfo('moved to pose 3')

if __name__ == '__main__':
    rospy.init_node('send_goal')
    x =sending_goal()
    x.sending()
