#!/usr/bin/env python3

import pifacedigitalio as pfio
from time import sleep
pfio.init()
piface = pfio.PiFaceDigital()
piface.output_pins[0].turn_on()  # this command does the same thing...
#pifacedigital.leds[0].turn_on()  # ...as this command...
#pifacedigital.relays[0].turn_on()  # ...and this 
sleep(7)


piface.output_pins[0].turn_off()
#piface.output_pins[0].turn_on()  # this command does the same thing...
sleep(1)
