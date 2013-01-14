'''
Created on 29.07.2012

@author: hamann
'''

import serial
import time

class MotorController(object):

    def __init__(self, serialport):
        # Neue Verbindung zum Serial-Port herstellen
        self.__serial = serial.Serial(serialport)
        # warte 5 sekunden, bis serial-port aktiv ist
        time.sleep(2)
        
        # Initial-Werte setzen: Vorwaerts, Speed 0, Bremse ein
        self.__brakeA = '1'
        self.__speedA = '000'
        self.__directionA = '0'
        self.__brakeB = '1'
        self.__speedB = '000'
        self.__directionB = '0'
        
    def __del__(self):
        # Serial-Port freigeben
        self.__serial.close()
        
    def drive(self, pDirection, pSpeed):
        # Richtung der Motoren setzen
        self.__directionA = str(pDirection)
        self.__directionB = str(pDirection)
        
        # Geschwindigkeit der Motoren setzen, ggf. dreistellig machen
        self.__speedA = str(pSpeed)
        self.__speedB = str(pSpeed)
        while (len(self.__speedA)<3):
            self.__speed = '0' + self.__speed
        while (len(self.__speedB)<3):
            self.__speed = '0' + self.__speed
        
        # Motoren setzen
        print self.__setMotor()
    
    def setBrake(self):
        if (self.__brakeA == '0'):
            self.__brakeA = '1'
        else:
            self.__brakeA = '0'   
        if (self.__brakeB == '0'):
            self.__brakeB = '1'
        else:
            self.__brakeB = '0'  
        print self.__setMotor()
        
    def __setMotor(self):
        vMotorA = '0' + self.__directionA + self.__brakeA + self.__speedA
        vMotorB = '1' + self.__directionB + self.__brakeB + self.__speedB
        vMotorCmd = vMotorA + '\n' + vMotorB + '\n'
        print vMotorCmd
        self.__serial.write(vMotorCmd)
        vReturn = self.__serial.readline()
        vReturn += self.__serial.readline()
        return vReturn
    
    def turn(self, pDirection, pSpeed):
        if (pDirection == 'left'):
            self.__directionA = '1'
            self.__directionB = '0'
            self.__speedA = str(pSpeed)
            self.__speedB = str(pSpeed)
        elif (pDirection == 'right'):
            self.__directionA = '0'
            self.__directionB = '1'
            self.__speedA = str(pSpeed)
            self.__speedB = str(pSpeed)
        print self.__setMotor()
        
    # Getter
    def getBrakeA(self):
        return self.__brakeA
        
    def getSpeedA(self):
        return self.__speedA
        
    def getDirectionA(self):
        return self.__directionA
        
    def getBrakeB(self):
        return self.__brakeB
    
    def getSpeedB(self):
        return self.__speedB
    
    def getDirectionB(self):
        return self.__directionB
            