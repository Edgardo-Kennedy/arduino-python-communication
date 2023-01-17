# arduino-python-communication
Arduino code and a python script that allow for dynamic, two way communication between an arduino board and your computer through the usb cable without blocking from either part and without the need for them to take turns sending messages.


Currently, the arduino has a microswitch and an LED hooked up to it. If the microswitch is pressed, the arduino sends an integer to the computer that increases by one everytime the switch is pressed. Meanwhile, from the computer you can tell the arduino to turn the LED on and off by sending the appropriate message.

These processes are obviously very simple. The point of this code is to provide the general structure for two way communication without blocking and without turns for your projects. The LED and Microswitch setup can be replaced with way more complex circuits. Similarly, the python script can be made to execute more complex tasks depending on the information it gathers from your arduino.
