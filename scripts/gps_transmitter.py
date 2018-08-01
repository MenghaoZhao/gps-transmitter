#!/usr/bin/env python

from novatel_msgs.msg import *
from middleware import Publisher, Subscriber, init_node, spin, start_heartbeat
from ts_rpc.client import RemoteObject, find_rpc_service
import time

class gps_transmitter():

    def __init__(self):
        gps_sub = Subscriber("/novatel_data/inspvax", INSPVAX)
        gps_sub.add_callback(self._callback)
	self.vm = find_rpc_service('vm')

    def _callback(self, data):
        latitude = data['/novatel_data/inspvax'].latitude
        longitude = data['/novatel_data/inspvax'].longitude
        self.vm.vehicle.set_gps('Octopus-B1', [latitude, longitude])


if __name__ == '__main__':
    init_node('gps_transmitter')
    start_heartbeat()
    g1 = gps_transmitter()
    spin()
