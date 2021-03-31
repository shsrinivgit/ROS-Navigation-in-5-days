#! /usr/bin/env python

import rospy
from nav_msgs.srv import GetPlan, GetPlanRequest

rospy.init_node('making_plan')
rospy.wait_for_service('/move_base/make_plan')
serv = rospy.ServiceProxy('/move_base/make_plan',GetPlan)
srv_object = GetPlanRequest()
srv_object.goal.pose.position.x = 1.16
srv_object.goal.pose.position.y = -4.76
srv_object.goal.pose.position.z = 0.0
srv_object.goal.pose.orientation.z = 0.75
srv_object.goal.pose.orientation.w = 0.66
srv_object.goal.header.frame_id = 'map'
result = serv(srv_object)
print(result)


