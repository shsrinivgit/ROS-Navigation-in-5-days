#! /usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult
from geometry_msgs.msg import PoseWithCovarianceStamped
import actionlib
import os
import rosparam
class task4():
    feedback = MoveBaseFeedback()
    def __init__(self):
        self.client = actionlib.SimpleActionClient('/move_base',MoveBaseAction)
        self.pose = PoseWithCovarianceStamped()
        rospy.loginfo('wait_for_server')
        self.client.wait_for_server()
        rospy.loginfo('server found')
        self.goal = MoveBaseGoal()
        rospy.sleep(0.5)
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.z = 0
        self.goal.target_pose.pose.orientation.x = 0
        self.goal.target_pose.pose.orientation.y = 0
        

    def file_open(self):
        os.chdir("/home/user/catkin_ws/src/navigation_exam/params")
        paramlist=rosparam.load_file("task2.yaml",default_namespace=None)

        for params,ns in paramlist: #ns,param
 
            for key, value in params.items():
                rosparam.upload_params(ns,params)
                return self.point(key,value)

    def point(self,key,val):
        if key == "point1":
            self.goal.target_pose.pose.position.x = val['position']['x']
            self.goal.target_pose.pose.position.y = val['position']['y']
            self.goal.target_pose.pose.orientation.z = val['orientation']['z']
            self.goal.target_pose.pose.orientation.w = val['orientation']['w']
            return self.goal

        elif key == "point2":
            self.goal.target_pose.pose.position.x = val['position']['x']
            self.goal.target_pose.pose.position.y = val['position']['y']
            self.goal.target_pose.pose.orientation.z = val['orientation']['z']
            self.goal.target_pose.pose.orientation.w = val['orientation']['w']
            return self.goal
    
    def callback(self, feedback):
        print(feedback)
    
    def sending(self):
        while not rospy.is_shutdown():
            goal = self.file_open()
            print(goal)
            self.client.send_goal(goal, feedback_cb=self.callback)
            self.client.wait_for_result()
            rospy.loginfo('moved to point 1')

            goal = self.file_open()
            self.client.send_goal(goal,feedback_cb=self.callback)
            self.client.wait_for_result()
            rospy.loginfo('moved to point 2')
        



if __name__=="__main__":
    rospy.init_node('sending_goal')
    x = task4()
    x.sending()