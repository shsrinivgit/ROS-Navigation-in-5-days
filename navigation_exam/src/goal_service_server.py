#! /usr/bin/env python

import rospy
from navigation_exam.srv import SendPosition, SendPositionResponse
from geometry_msgs.msg import PoseWithCovarianceStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback
import actionlib
from send_goals import task4
import os
import rosparam

class task5():
    feedback = MoveBaseFeedback
    def __init__(self):
        self.serv = rospy.Service('/send_pose_service',SendPosition,self.srv_callback)
        self.client = actionlib.SimpleActionClient('/move_base',MoveBaseAction)
        self.goal = MoveBaseGoal()
        self.pose = PoseWithCovarianceStamped()
        self.action = task4()
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.z = 0
        self.goal.target_pose.pose.orientation.x = 0
        self.goal.target_pose.pose.orientation.y = 0
        rospy.sleep(0.5)

    def srv_callback(self, request):
        resp = SendPositionResponse()
        labl = request.label
        key, val = self.file_open()
        if key == labl:
            goal = self.action.point(key,val)
        elif key == labl:
            goal = self.action.point(key,val)
        else:
            print('error')
        self.client.send_goal(goal,feedback_cb=self.feedback_callbk)
        rospy.loginfo('sending goal')
        resp.navigation_successfull = True
        resp.message = "OK" 
        return resp

    def feedback_callbk(self, feedback):
        print(feedback)

    def file_open(self):
        os.chdir("/home/user/catkin_ws/src/navigation_exam/params")
        paramlist=rosparam.load_file("task2.yaml",default_namespace=None)

        for params,ns in paramlist: #ns,param
 
            for key, value in params.items():
                rosparam.upload_params(ns,params)
                return key,value

if __name__=="__main__":
    rospy.init_node('goal_server')
    task5()
    rospy.spin()
