#! /usr/bin/env python

import rospy
from my_turtlebot_localization.srv import MyServiceMessage, MyServiceMessageResponse
from geometry_msgs.msg import PoseWithCovarianceStamped
class spot_service():
    def __init__(self):
        self.service = rospy.Service('/save_spot',MyServiceMessage,self.serv_callback)
        self.sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.callback)
        self.pose = PoseWithCovarianceStamped()
        self.save_poses = []
        rospy.sleep(1)

    def serv_callback(self, request):
        result = MyServiceMessageResponse()
        if request.label=="corner1":
            self.save_poses.append(self.pose.pose.pose)
        elif request.label=="corner2":
            self.save_poses.append(self.pose.pose.pose)
        elif request.label=="pedestrian":
            self.save_poses.append(self.pose.pose.pose)
        elif request.label=="end":
            f = open("MyPoses.yaml","w")
            f.write(str(self.save_poses))
            f.close()

        print(self.save_poses)
        result.navigation_successfull = True
        result.message = "Success"
        return result

    def callback(self, msg):
        self.pose = msg
        return self.pose

if __name__=="__main__":
    rospy.init_node("spot_recorder")
    spot_service()
    rospy.spin()