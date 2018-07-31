#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import middleware as mw
from middleware import Publisher, Subscriber, SmartMixer, Timer, run_handler_async, Duration, FunctionMonitor, \
    init_node, spin, start_heartbeat
from ts_rpc.client import RemoteObject
import time

class gps_transmitter():

    def __init__(self):
	gps_sub = rospy.Subscriber('novatel_gps', String, self._callback)
	#gps_sub.add_callback(self._callback)
	print('call back added')
        self.vm = RemoteObject('http://0.0.0.0:5023')

    def _callback(self, data):
        latitude = str(data).split('latitude:')[1].split("\\n")[0]
        longitude = str(data).split('longitude:')[1].split("\\n")[0]
       # print(str(data))
	print('in call back')
        print(latitude)
        print(longitude)
        self.vm.vehicle.set_gps('Octopus-B1', [float(time.time())])


if __name__ == '__main__':
    rospy.init_node('gps_transmitter')
    #start_heartbeat()
    g1 = gps_transmitter()
    rospy.spin()
