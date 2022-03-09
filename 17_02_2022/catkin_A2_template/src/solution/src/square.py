#!/usr/bin/env python
import rospy
from geometry_msgs.msgs import Twist
from std_msgs.msgs import Float32

class square():
    __pubcdm = None
    __subwr = None
    __subwl = None
    def __init__(self):
        rospy.init_node('square')
        self.__pubcmd = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.__subwl = rospy.Subscriber('/wl', Float32, callback=self.callback)
        self.__subwr = rospy.Subscriber('/wr', Float32, callback=self.callback)

    def callback(self):
        while not rospy.is_shutdown():
            seconds = rospy.get_time()

    def main(self):
        rospy.spin()



if __name__ == '__main__':
    square()
