'''
Created on 30.07.2012

@author: hamann
'''

from tinkerforge.ip_connection import IPConnection

class Sensors(object):

    def __init__(self):
     self.__ipcon = IPConnection('localhost', 4223)
     
    def __del__(self):
        self.__ipcon.destroy()
        
    def add(self, pSensor):
        self.__ipcon.add_device(pSensor)
        