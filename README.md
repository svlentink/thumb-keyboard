# Thumb keypad keyboard

status: WIP

## Idea

The future will include smart glasses.
Companies are pushing us to using voice for interaction with our devices.

Personally, I don't like this.
E.g. when the smelly sweaty guy in the subway remembers you to add deodorant to your shopping list,
you won't say "OK Google, remember me to buy deodorant".
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

The basic keypads do not come with diodes,
making it
[unable to distinguish](https://electronics.stackexchange.com/questions/114993/pressing-same-key-rows-at-the-same-time)
between any
way of pressing 3 or 4 buttons pressed on a 2by2 matrix.
Therefore, for every board,
we have every one unique button (4)
and any combinations of two buttons pressed at once (6)
minus the diagonals (2) since pressing them is hard,
and pressing any 3 or 4 buttons simultaneously (1).
Resulting in `4 + 6-2 + 1 = 9` different input values.
Using two matrices results in `9*9-1=80`,
the one is deducated to switch between keyboard and mouse mode.

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

### Old wiring based on board with diodes (which we do not have atm.)

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

### Actual wiring, based on board without diodes

We used the
[following](https://www.raspberrypi.org/documentation/usage/gpio/)
set of pins:

| | pins | GPIO | loc |
| --- | --- | --- | --- |
| ROW1 L | LTL1 | 9 | 21 |
| ROW2 L | LTL2 | 25 | 22 |
| COL1 | LTR2 | 11 | 23 |
| COL2 | LTR1 | 8 | 24 |
| ROW1 R | RTL2 | 5 | 29 |
| ROW2 R | RTL1 | 6 | 31 |
| COL3 | RTR1 | 13 | 33 |
| COL4 | RTR2 | 19 | 35 |

No need for a
[resistor](https://www.freecodecamp.org/news/a-simple-explanation-of-pull-down-and-pull-up-resistors-660b308f116a/)
since we enabling it using
[pull down](https://raspi.tv/2013/rpi-gpio-basics-6-using-inputs-and-outputs-together-with-rpi-gpio-pull-ups-and-pull-downs)
(thus down in software).


## Key layout

We assume a standard US keyboard layout
(with pipe `|` button between backspace and enter).
Each type has it's own additionals;
command for Mac,
search for chromebook
and start for Windows.
The common larger buttons are;
space, backspace, enter, tab, shift, ctrl and alt.
These larger buttons mean they are used more often.
Of which shift, ctrl and alt are buttons that are to remain pressed
(or simulated) when following through with another input.

Since I'm not a UX designer, the code should/will
enable someone to model different ways of interaction/behavior
without needing to change the code.

## Possibility to distinguish 3 button pressed

After testing our initial prototype,
we discovered that when you press two buttons at the same time on one matrix,
release one and hold one down and than press another,
we do can distinguish 3 buttons pressed per matrix.
Not sure if we want this though.

