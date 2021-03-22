#! /usr/bin/env python

import rospy
from nav_msgs.srv import GetMap, GetMapRequest

rospy.init_node('service_clien')

rospy.wait_for_service('/static_map')
call_the_ser = rospy.ServiceProxy('/static_map',GetMap)
serv_object = GetMapRequest()
result = call_the_ser(serv_object)
print(result)