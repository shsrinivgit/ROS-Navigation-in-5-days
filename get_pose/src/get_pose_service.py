#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import PoseWithCovarianceStamped
class get_pose():
    def __init__(self):
        self.serv = rospy.Service('/get_pose',Empty,self.serv_callback)
        self.sub = rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,self.callback)
        self.pose = PoseWithCovarianceStamped()
        rospy.sleep(1)
    
    def callback(self,msg):
        self.pose = msg.pose
        return self.pose

    def serv_callback(self,request):
        resp = EmptyResponse()
        print(self.pose)
        return resp

if __name__=="__main__":
    rospy.init_node('get_pose')
    x = get_pose()
    rospy.spin()