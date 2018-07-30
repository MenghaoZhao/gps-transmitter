#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import middleware as mw
from middleware import Publisher, Subscriber, SmartMixer, Timer, run_handler_async, Duration, FunctionMonitor, \
    init_node, spin, start_heartbeat

class gps_transmitter():

    def __init__(self):
        gps_sub = rospy.Subscriber("novatel_gps", String, self._callback)

    def _callback(self, data):
        print(data)


if __name__ == '__main__':
    init_node('gps_transmitter')
    start_heartbeat()
    gps_transmitter()
    spin()
