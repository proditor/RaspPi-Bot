'''
Created on 31.07.2012

@author: hamann
'''

from MotorControl.MotorController import *
from Sensors.Sensors import *
from Sensors.DistanceSensor import *
import time

class Robot(object):

    def cb_sensorFront(self, param):
        '''
        Callback-Function for front-sensor. In this we manage not hitting anything.
        @param param: given by tinkerforge
        '''
        # wenn abstannd nach vorne zu kurz?
        motorAbreak = self.__motor.getBrakeA()
        motorBbreak = self.__motor.getBrakeB()
        motorAdirection = self.__motor.getDirectionA()
        motorBdirection = self.__motor.getDirectionB()
        motorAspeed = self.__motor.getSpeedA()
        motorBspeed = self.__motor.getSpeedB()
        
        # pfuefen, ob er ueberhaupt faehrt, und nicht im turn drin ist
        
        if (motorAbreak == '1') or (motorBbreak == '1') or (motorAspeed == '000') or (motorBspeed == '000') or (motorAdirection != motorBdirection):
            print 'nothing to do ...'
            return
        
        self.__motor.setBrake()
        time.sleep(0.5)
        
        if (self.__lastTurn == 'l'):
            self.__motor.turn('right', 255)
            self.__lastTurn = 'r'
        else:
            self.__motor.turn('left', 255)
            self.__lastTurn = 'l'
        self.__motor.setBrake()
        while (self.__sensorFront.getDistance() < 300):
            time.sleep(0.2)
        self.__motor.setBrake()
        
        self.__motor.drive(0, 255)
        self.__motor.setBrake()
        

    def __init__(self):
        '''
        Constructor for new robot. Creates connection to motor-controller, tinkerforge, and creates the necessary sensor-object
        '''
        #self.__motor = MotorController('/dev/tty.usbmodemfd141')
        self.__motor = MotorController('/dev/ttyACM0')
        self.__sensors = Sensors()
        self.__sensorFront = DistanceSensor('9t7', self.__sensors)
        self.__sensorFront.setDistanceCallback(2000, self.cb_sensorFront, '<', 150, 0) # debounce so einstellen, dass Ungenauigkeiten wg. Spannung an der tinkerforge ausgeglichen werden
        
        self.__lastTurn = 'l'
        
    def __del__(self):
        '''
        Frees the sensors and motor-controller
        '''
        del self.__sensors
        del self.__motor
        
    def getMotor(self):
        '''
        Returns the motor-controller-object
        '''
        return self.__motor
    
    def getSensors(self):
        '''
        Returns the tinkerforge-object
        '''
        return self.__sensors
    
    def getSensorFront(self):
        '''
        Returns the front-senssor-object
        '''
        return self.__sensorFront
    
    def start(self):
        '''
        Start the robot. makes him drive forward at full-speed
        '''
        self.__motor.drive(0, 255)
        self.__motor.setBrake()
        
    def stop(self):
        '''
        Stop the robot. Basically, only toggles the brakes.
        '''
        if (self.__motor.getBrakeA() != '1') or (self.__motor.getBrakeB() != '0'):
            self.__motor.setBrake()
        else:
            self.__motor.drive(0, 0)