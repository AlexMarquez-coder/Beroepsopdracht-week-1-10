        # Add your Python code here. E.g.

from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll('Alex')
    if button_b.is_pressed():
        display.show(Image('00900:'
                   '09990:'
                   '09990:'
                   '00900:'
                   '00900'))
