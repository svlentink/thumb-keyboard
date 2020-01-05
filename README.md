# Thumb keypad keyboard

status: WIP

## Idea

The future will include smart glasses.
Companies are pushing use to using voice for interaction with our devices.

Personally, I don't like this.
E.g. when the smelly sweaty guy in the subway remembers that you needed to buy deodorant,
you don't say "OK Google, remember me to buy deodorant".
Typing allows for more private interaction with your device.

### History

I've explored using a joystick and 3 by 3 matrix of buttons.
But 2 by 2 is the easiest, cheapest, lightest and smallest,
making it the best fit for this project.

### Concept

Both thumbs rest on a **2x2 button matrix**.
If you press all 8 buttons at once,
you switch between keyboard and mouse mode.

In mouse mode, one thumb controls the cursor,
the other is for right/left click
and scroll up/down.

In keyboard mode, various combinations of buttons
produce various characters/key actions
(in theory `2^8-2` options).
The keystroke is only registred if all buttons
are springed back again.
Thus pressing one or more buttons slightly later
does not matter.

## Wiring

We take the following physical layout:
```
    Left thumb             Right thumb
    _____________        _____________
   |O   _   _   O|      |O   _   _   O|
---|L1 |o| |o|   |      |   |o| |o| R2|---
---|L2           |      |           R1|---
---|R1  _   _    |      |    _   _  L2|---
---|R2 |o| |o|   |      |   |o| |o| L1|---
   |O___________O|      |O___________O|
```
We will prefix the pin names with LT for left thumb
and RT for right thumb.

Which we image to be rows and colums:
```
       C1   C2              C3   C4
        _   _                _   _
ROW1   |o| |o|              |o| |o|

        _   _                _   _
ROW2   |o| |o|              |o| |o|
```

We observe that the ROWs span across both the Left as the Right keypad.
We therefore string these together;
LTL1 together with RTL2 and LTL2 with RTL1.
This gives us the following table:

| | pins | GPIO |
| --- | --- | --- |
| ROW1 | LTL1, RTL2 | 23 |
| ROW2 | LTL2, RTL1 | 24 |
| COL1 | LTR2 | 5 |
| COL2 | LTR1 | 6 |
| COL3 | RTR1 | 13 |
| COL4 | RTR2 | 19 |

For the ROWs we combine the two cables we attach to the pins,
connect it to a [resistor](https://www.raspberrypi.org/forums/viewtopic.php?t=211657#p1306345)
and then connect it to the GPIO.
```
LTL1--
      \
       |--\/\/\--GPIO
      /
RTL2--
```


## Links

- https://raspberrypi.stackexchange.com/questions/53665/how-to-use-a-4x4-keypad-in-python
- https://maker.pro/raspberry-pi/tutorial/how-to-use-a-keypad-with-a-raspberry-pi-4
- https://tutorials-raspberrypi.com/connecz-raspberry-pi-kecpad-code-lock/
- https://learn.adafruit.com/matrix-keypad?view=all
- https://tutorials-raspberrypi.de/raspberry-pi-keypad-tastatur/

