#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_srvs.srv import Empty, EmptyRequest
class move_square():
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub = rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped, self.callback)
        self.move= Twist()
        self.cov = PoseWithCovarianceStamped()
        rospy.sleep(1)
    
    def serv_client(self):
        wait = rospy.wait_for_service('/global_localization')
        serv_clie = rospy.ServiceProxy('/global_localization',Empty)
        req = EmptyRequest()
        result = serv_clie(req)

    def sqr_mov(self):
        self.serv_client()
        rospy.sleep(1)
        print(self.cov.pose.covariance)
        z = (self.cov.pose.covariance[0] + self.cov.pose.covariance[7] + self.cov.pose.covariance[-1])
        print('cov',z)
        count = 4
        while count>0:
            self.move_straight()
            rospy.sleep(0.1)
            self.rotate()
            rospy.sleep(0.1)
            count -=1
            z = (self.cov.pose.covariance[0] + self.cov.pose.covariance[7] + self.cov.pose.covariance[-1])
            print(self.cov.pose.covariance)
            print('cov2',z)
        if z<0.65:
            print('Robot localized itself')
            print(z)
        else:
            self.sqr_mov()
        
    
    def move_straight(self):
        count =35
        while count >0:
            self.move.linear.x = 0.5
            self.move.angular.z = 0
            self.pub.publish(self.move)
            rospy.sleep(0.1)
            count -= 1

    def rotate(self):
        count =25
        while count >0:
            self.move.linear.x = 0.1
            self.move.angular.z = 0.7
            self.pub.publish(self.move)
            rospy.sleep(0.1)
            count -= 1
    def callback(self, msg):
        self.cov = msg
        return self.cov

if __name__=="__main__":
    rospy.init_node('husky_square')
    x = move_square()
    x.sqr_mov()
