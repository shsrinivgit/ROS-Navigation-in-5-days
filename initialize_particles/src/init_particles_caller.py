#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node("init_particl")
wait = rospy.wait_for_service('/global_localization')
serv_clie = rospy.ServiceProxy('/global_localization',Empty)
req = EmptyRequest()
result = serv_clie(req)
print(result)

rospy.spin()