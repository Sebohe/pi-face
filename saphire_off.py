import pifacedigitalio as pfio
from time import sleep
pfio.init()
piface = pfio.PiFaceDigital()
piface.output_pins[1].turn_on()  # this command does the same thing...
sleep(7)
piface.output_pins[1].turn_off()
sleep(1)
