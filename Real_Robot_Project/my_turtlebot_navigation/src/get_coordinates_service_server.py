#! /usr/bin/env python

import rospy
from my_turtlebot_localization.srv import MyServiceMessage, MyServiceMessageResponse
from geometry_msgs.msg import PoseWithCovarianceStamped
import actionlib
from send_coordinates_action_client import recv_coords
import os
import rosparam

class Move_service():
    def __init__(self):
        self.serv = rospy.Service('/get_coordinates',MyServiceMessage,self.srv_callback)
        self.ac = recv_coords()
        rospy.sleep(0.5)
        
    def srv_callback(self,request):
        resp = MyServiceMessageResponse()
        # x = open("/home/user/catkin_ws/src/shsriniv_nav5/Real_Robot_Project/my_turtlebot_localization/src" + "/MyPoses.yaml")
        # reading = x.read()
        os.chdir("/home/user/catkin_ws/src/shsriniv_nav5/Real_Robot_Project/my_turtlebot_localization/src")
        paramlist=rosparam.load_file("spots.yaml",default_namespace=None)

        for params,ns in paramlist:
            for key, value in params.items():
                if key == request.label:
                    rosparam.upload_params(ns,params) #ns,param
                    val = value
        self.ac.get_coords(value)
        rospy.loginfo('sending the coordinates to action client')
        resp.navigation_successfull = True
        resp.message = "OK"
        return resp
    
if __name__ == "__main__":
    rospy.init_node('service_serv')
    Move_service()
    rospy.spin()

    

        