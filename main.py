#!/usr/bin/env python3

from pad4pi import rpi_gpio # https://github.com/brettmclean/pad4pi
import RPi.GPIO as GPIO
import time

GPIO.cleanup()


def onKeyPress(self, channel):
  keyPressed = self.getKey()
  print(keyPressed)
rpi_gpio.Keypad._onKeyPress = onKeyPress

def setRowsAsInput(self):
    # Set all rows as input
    for i in range(len(self._row_pins)):
        GPIO.setup(self._row_pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self._row_pins[i], GPIO.BOTH, callback=self._onKeyPress, bouncetime=rpi_gpio.DEFAULT_DEBOUNCE_TIME)
rpi_gpio.Keypad._setRowsAsInput = setRowsAsInput


KEYPAD = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

ROW_PINS = [23, 24] # BCM numbering
COL_PINS = [5, 6, 13, 19] # BCM numbering

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(
  keypad=KEYPAD,
  row_pins=ROW_PINS, #gpio_mode=GPIO.BCM,
  col_pins=COL_PINS,
  key_delay=100,
  repeat=True,
  repeat_delay=1,
  repeat_rate=1)

def printKey(key):
    print(key)

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

while True:
  time.sleep(1)
