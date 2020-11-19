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
    def __add_mapping(self, k, v):
        if '?' in k:
            for i in range(len(k)):
                if k[i] is '?':
                    pre = k[:i]
                    post = k[i+1:]
                    self.__add_mapping(pre + '0' + post, v)
                    self.__add_mapping(pre + '1' + post, v)
                    return
        else:
            if k not in self.__map:
                self.__map[k] = v
            else:
                print('WARNING duplicate key in keybinding',k)

    def __init__(self, mapping_file='keybindings/example.yml'):
        self.__action = self.__key_action
        self.__memory = ''
        self.__map = {}
        with open(mapping_file, 'r') as f:
            raw = f.read()
        obj = load(raw)
        for k,v in obj.items():
            self.__add_mapping(k,v)

    def binary2action(self,inp):
        # switch between keyboard/mouse if all buttons are pressed
        if inp.count('0') == 0:
            if self.__action is self.__key_action:
                self.__action = self.__mouse_action
            else:
                self.__action = self.__key_action
        else:
            self.__action(inp)

    def __key_action(self, inp):
        if inp in self.__map:
            act = self.__map[inp]
        else:
            self.__memory = ''
            print('WARNING: combination not in mapping',inp)
            return
        if 'hold' in act and act['hold']:
            self.__memory = self.__memory + act['action'] + '+'
            return
        else:
            press = self.__memory + act['action']
            self.__memory = ''
            print('INFO pressing',press)
            keyboard.send(press)

    def __mouse_action(self, inp):
        return None


