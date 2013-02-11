'''
Created on 29.07.2012

@author: hamann
'''

from MotorController import *
import time

if __name__ == '__main__':
    # Serial-Port auf dem Raspberry
    m = MotorController('/dev/ttyACM0')
     
    print 'Wir fahren erstmal geradeaus'
    #fahren
    m.drive(0, 150)
    m.setBrake()
    time.sleep(5)
    
    #stopp
    m.setBrake()
    time.sleep(2)
    
     
    print 'Dann drehen wir uns etwas nach links'
    #fahren
    m.turn('left', 150)
    m.setBrake()
    time.sleep(3)
    
    #stopp
    m.setBrake()
    time.sleep(2)
    
    print 'und fahren wieder geradeaus weiter'
    #fahren
    m.drive(0, 150)
    m.setBrake()
    time.sleep(5)
    
    #stopp
    m.setBrake()
    time.sleep(2)
    
    print 'ein wenig im kreis drehen'
    m.turn('right', 255)
    m.setBrake()
    time.sleep(4)
    
    print 'und stopp'
    m.setBrake()
    