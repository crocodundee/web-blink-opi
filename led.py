from pyA20.gpio import gpio
from pyA20.gpio import port

class Led(object):
    def __init__(self, pinNum):
        self.ledPin = pinNum
        gpio.init()
        gpio.setcfg(self.ledPin, gpio.OUTPUT)

    def lightOn(self):
        gpio.output(self.ledPin, 1)

    def lightOff(self):
        gpio.output(self.ledPin, 0)


