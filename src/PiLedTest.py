import socket
import time
from time import sleep
from PiDemo import blink_led

from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_dc_motor as dc_motor
from hal import hal_buzzer as buzzer
from hal import hal_servo as servo
from hal import hal_input_switch as switch
import version as ver

def switch_check():
    switch.init()
    if(switch.read_slide_switch() == 1):
        blink_led(0.1)
    
    elif(switch.read_slide_switch() == 0):
        for x in range(25):
            blink_led(0.05)
        while(switch.read_slide_switch() == 0):
            led.set_output(0, 0)
    
def main():
    
    
    while(1):
        switch_check()

    
if __name__ == "__main__":
    main()