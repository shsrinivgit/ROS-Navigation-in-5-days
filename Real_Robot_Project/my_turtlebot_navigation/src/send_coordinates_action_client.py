#! /usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal,MoveBaseResult,MoveBaseFeedback
import actionlib
from geometry_msgs.msg import Pose
import rosparam

class recv_coords():
    feedback = MoveBaseFeedback()
    def __init__(self):
        feedback = MoveBaseFeedback()
        self._as = actionlib.SimpleActionClient('/move_base',MoveBaseAction)
        rospy.loginfo('connecting')
        self._as.wait_for_server()
        rospy.loginfo('server_connected')
        self.goal = MoveBaseGoal()
        rospy.sleep(0.1)
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.z = 0
        self.goal.target_pose.pose.orientation.x = 0
        self.goal.target_pose.pose.orientation.y = 0
    
    def get_coords(self, coords):
        values = coords
        while not rospy.is_shutdown():
            self.goal.target_pose.pose.position.x = values['position']['x']
            self.goal.target_pose.pose.position.y = values['position']['x']
            self.goal.target_pose.pose.orientation.z = values['orientation']['z']
            self.goal.target_pose.pose.orientation.w = values['orientation']['w']
            print(self.goal)
            self._as.send_goal(self.goal, feedback_cb=self.feedback_callbak)
            self._as.wait_for_result()
            rospy.loginfo('moved to location')
            
    def feedback_callbak(self, feedback):
        print(feedback)
        

if __name__=='__main__':
    rospy.init_node('action_client')
    recv_coords()
    rospy.spin()




