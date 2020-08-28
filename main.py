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
  GPIO.setmode(GPIO.BCM)
  for boardi in pins:
    board = pins[boardi]
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
      callback(state)
      state = set()


def coord2binary(inp):
  result = ''
  for y in range(2):
    for x in range(4):
      coord = (x, y)
      result += str(int(coord in inp))
  return result


def visualize_buttons(s):
  a = s.replace('1','X')
  row1 = '  '.join( list( a[:4] ) )
  row2 = '  '.join( list( a[-4:] ) )
  print('')
  print('')
  print(row1)
  print('')
  print(row2)
  print('')


def callback(inp):
  bin = coord2binary(inp)
  visualize_buttons(bin)


try:
  init(pins)
  monitoring(pins,callback)
finally:
  GPIO.cleanup()

