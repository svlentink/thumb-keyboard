#!/usr/bin/env python3

from actions import (Action,visualize_buttons)
from btnwatcher import Btnwatcher


def coord2binary(inp):
  result = ''
  for y in range(2):
    for x in range(4):
      coord = (x, y)
      result += str(int(coord in inp))
  return result


a = Action()

for inp in Btnwatcher():
  binary = coord2binary(inp)
  visualize_buttons(binary)
  a.binary2action(binary)


