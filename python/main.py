'''
Created on 31.07.2012

@author: hamann
'''

from Robot import *
import time

if __name__ == '__main__':
    pi = Robot()
    time.sleep(5) # sonst wird das callback nicht registriert
    pi.start()
    raw_input('Press key to exit\n')
    pi.stop()
    del pi