#!/usr/bin/env python3

import pifacedigitalio as pfio
from time import sleep


pfio.init()
piface = pfio.PiFaceDigital()

while True:
    saphireButton = piface.switches[0].value
    gtxButton = piface.switches[3].value
    
    

    if gtxButton:
        piface.output_pins[0].turn_on()
    else:
        piface.output_pins[0].turn_off()

       
    if saphireButton:
        piface.output_pins[1].turn_on()
    else:
        piface.output_pins[1].turn_off()

