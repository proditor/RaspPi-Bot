'''
Created on 30.07.2012

@author: hamann
'''

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir import DistanceIR

class DistanceSensor(object):

    def __init__(self, pID, pSensor):
        '''
        Constructor for new DistanceSensor
        @param pID: string the id of the IR-Sensor-Module (check with brickv)
        @param pSensor: the Sensors-Object to attach to.
        '''
        self.__id = pID
        self.__dist = DistanceIR(self.__id)
        pSensor.add(self.__dist)
        
    def getDistance(self):
        '''
        Return the actual distance, in mm
        @return int: Distance in mm
        '''
        return self.__dist.get_distance()
    
    def setDistanceCallback(self, pDebouncePeriod, pCallbackFunction, pOperator, pMin, pMax):
        '''
        
        @param pDebouncePeriod: int
        @param pCallbackFunction: function
        @param pOperator: string
        @param pMin: int
        @param pMax: int
        '''
        self.__dist.set_debounce_period(int(pDebouncePeriod))
        
        self.__dist.register_callback(self.__dist.CALLBACK_DISTANCE_REACHED, pCallbackFunction)
        self.__dist.set_distance_callback_threshold(pOperator, int(pMin), int(pMax))