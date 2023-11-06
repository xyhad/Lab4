from hal import hal_input_switch as switch
from hal import hal_led as led
import time
from time import sleep

def blinky():
    led.init()
    status=switch.read_slide_switch()
    i=0
    while 1:
        i=0
        while status==1:
            led.set_output(0, 1)
            time.sleep(0.25)
            led.set_output(0, 0)
            time.sleep(0.25 )
            status=switch.read_slide_switch()

        while status==0:
            if i<=20:
                led.set_output(0, 1)
                time.sleep(0.125)
                led.set_output(0, 0)
                time.sleep(0.125)
                i+=1
            else:
                led.set_output(0, 0)    
            status=switch.read_slide_switch()

def main():
    switch.init()
    blinky()

# Main entry point
if __name__ == "__main__":
    main()