#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from novatel_msgs.msg import *
import middleware as mw
from middleware import Publisher, Subscriber, SmartMixer, Timer, run_handler_async, Duration, FunctionMonitor, \
    init_node, spin, start_heartbeat
from ts_rpc.client import RemoteObject
import time

class gps_transmitter():

    def __init__(self):
        gps_sub = Subscriber("novatel_data/inspvax", INSPVAX)
        #gps_sub_ros = rospy.Subscriber("novatel_gps", String, self._callback)
	gps_sub.add_callback(self._callback)
	self.vm = RemoteObject('http://0.0.0.0:5023')

    def _callback(self, data):
        latitude = data['novatel_data/inspvax'].latitude
        longitude = data['novatel_data/inspvax'].longitude
       # print(str(data))
        print(latitude)
        print(longitude)
        self.vm.vehicle.set_gps('Octopus-B1', [latitude, longitude])


if __name__ == '__main__':
    init_node('gps_transmitter')
    start_heartbeat()
    g1 = gps_transmitter()
    spin()
