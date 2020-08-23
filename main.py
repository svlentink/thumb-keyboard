#!/usr/bin/env python3

# GPIO pin numbers (which is BCM numbering)
pins = {
  'L' : {
    'rows' : (9,25),
    'cols' : (11,8),
  },
  'R' : {
    'rows' : (5,6),
    'cols' : (13,19),
  },
}


#from pad4pi import rpi_gpio # https://github.com/brettmclean/pad4pi/blob/develop/pad4pi/rpi_gpio.py
import RPi.GPIO as GPIO
from time import sleep


def init(pins):
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)
  for board in pins:
    for col in board['cols']:
      GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      # GPIO.add_event_detect
    for row in board['rows']:
      GPIO.setup(row, GPIO.OUT)

def monitoring(pins,callback=print):
  cols = pins['L']['cols'] + pins['R']['cols']
  state = set()
  while True:
    something_pressed = False
    for rowi in range(2):
      on = board['L']['rows'][rowi]
      off = board['R']['rows'][rowi-1]
      GPIO.output(on,1)
      GPIO.output(off,0)

      sleep(0.02)

      for coli in range(len(cols)):
        pin = cols[coli]
        if GPIO.input(pin):
          pressed = str(coli) + str(rowi)
          state.add(pressed)
          something_pressed = True

    if not something_pressed:
      callback(state)
      state = set()


try:
  init(pins)
  monitoring(pins)
finally:
  GPIO.cleanup()

