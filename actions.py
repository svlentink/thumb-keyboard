#!/usr/bin/env python3

import keyboard
from yaml import load

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


class Action:
    def __init__(self, mapping_file='keybinding/example.yml'):
        self._action = self._key_action
        self._memory = ''
        with open(mapping_file, 'r') as f:
            raw = f.read()
            self.map = load(raw)

    def binary2action(self,inp):
        # switch between keyboard/mouse if all buttons are pressed
        if inp.count('0') == 0:
            if self._action is self._key_action:
                self._action = self._mouse_action
            else:
                self._action = self._key_action
        else:
            self._action(self,inp)

    def _key_action(self,inp):
        if inp in self.map:
            act = self.map[inp]
        else:
            self._memory = ''
            print('WARNING: combination not in mapping',inp)
            return
        if 'hold' in act and act['hold']:
            self._memory = self._memory + act['action'] + '+'
            return
        else:
            keyboard.send(self._memory + act['action'])
            self._memory = ''

    def _mouse_action(self,inp):
        return None


