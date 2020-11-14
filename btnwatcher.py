#!/usr/bin/env python3

# GPIO pin numbers (which is BCM numbering)
pinout = {
  'L' : {
    'rows' : (9,25),
    'cols' : (11,8),
  },
  'R' : {
    'rows' : (5,6),
    'cols' : (13,19),
  },
}

import RPi.GPIO as GPIO
from time import sleep


class Btnwatcher:

  def __init__(self, pins=pinout):
    self._pins = pins
    GPIO.setmode(GPIO.BCM)
    for boardi in pins:
      board = pins[boardi]
      for col in board['cols']:
        GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      for row in board['rows']:
        GPIO.setup(row, GPIO.OUT)
  
  def __iter__(self):
    return self

  def __next__(self):
    pins = self._pins
    cols = pins['L']['cols'] + pins['R']['cols']
    state = set()
    while True:
      something_pressed = False
      for rowi in range(2):
        on = pins['L']['rows'][rowi]
        off = pins['L']['rows'][rowi-1]
        GPIO.output(on,1)
        GPIO.output(off,0)
        on = pins['R']['rows'][rowi]
        off = pins['R']['rows'][rowi-1]
        GPIO.output(on,1)
        GPIO.output(off,0)
  
        sleep(0.02)
  
        for coli in range(len(cols)):
          pin = cols[coli]
          if GPIO.input(pin):
            pressed = (coli,  rowi)
            state.add(pressed)
            something_pressed = True
  
      if not something_pressed and state:
        return state
        state = set()

