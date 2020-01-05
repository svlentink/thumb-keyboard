
from pad4pi import rpi_gpio # https://github.com/brettmclean/pad4pi

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
  repeat_rate=5)

def printKey(key):
    print(key)

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)
