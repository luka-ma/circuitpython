# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
This code makes the servo rotate 180 degrees

Here's how you make code look like code:

```python
Code goes here
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("make it red!")
dot.brightness = 0.2
while True:
    dot.fill((255, 0, 0))


```


### Evidence
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
For this one all we had to change was then RGB settings and then the colrs were changing.

## CircuitPython_Servo

### Description & Code

```python
This code makes the servo rotate 180 degrees

Here's how you make code look like code:

```python
Code goes here
"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)


```

### Evidence

### Wiring

### Reflection
We found the code on the Circuit Python Servo website and pasted it onto the software. It took me a while to figure out how to hook the servo up to my board correctly but after that it started moving.




## CircuitPython_LCD

### Description & Code

```python
Code goes here
https://im.ezgif.com/tmp/ezgif-1-1483f9407511.gif


```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
